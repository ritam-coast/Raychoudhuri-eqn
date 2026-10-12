"""Reduced Raychaudhuri collapse model (derived closure), units 4*pi*G = 1.

Reconstructed from the project notes -- NOT the original analysis scripts, which
were lost when the working session was reset. Toy sigmoid EoS only.
"""
RC = 0.8
BUCHDAHL_X = 8.0 / 9.0

def eos(rho):
    x = (rho / RC) ** 4
    return rho * x / (1 + x)

def support(rho, R):
    """Volume-averaged acceleration divergence for a uniform-density GR interior."""
    X = (2.0 / 3.0) * rho * R ** 2
    return rho / max(1 - X, 1e-9), X, X >= BUCHDAHL_X

def terms(theta, rho, R):
    kin = -theta ** 2 / 3
    grav = -(rho + 3 * eos(rho))
    sup, X, violated = support(rho, R)
    return kin, grav, sup, kin + grav + sup, X, violated

def integrate(rho0, theta0, R0=1.0, dt=1e-3, tmax=16.0):
    rho, theta, R, t = rho0, theta0, R0, 0.0
    plateau = 0
    while t < tmax:
        kin, grav, sup, thd, X, violated = terms(theta, rho, R)
        if violated or rho >= 80 or theta <= -30 or R <= 1e-3:
            return "collapse", t
        theta += dt * thd
        rho += dt * (-theta * (rho + eos(rho)))
        R += dt * (theta * R / 3)
        t += dt
        plateau = plateau + 1 if (abs(theta) < 0.02 and t > 0.25) else 0
        if plateau > 300:
            return "stable", t
        if theta > 3 and t > 0.5:
            return "disperses", t
    return "undetermined", t

if __name__ == "__main__":
    for rho0, th0 in [(0.6, -0.1), (0.6, -1.0), (1.5, -0.1)]:
        print(rho0, th0, integrate(rho0, th0))
