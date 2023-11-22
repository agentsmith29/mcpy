import os
import sys

sys.path.append('./src')
import mcpy
import pandas as pd

from mcpy.BaseType.MCSamples import MCSamples

print(mcpy.version)
N = int((1 / (1 - 0.95)) * 10 ** 6)
print(f"N={N}")

# R21
R21_ = 100  # Ohm
delta_a_R21_ = (5e-3 * R21_) / 100  # Ohm
R21 = mcpy.Rectangular(R21_, delta_a_R21_)
#R21.mc_sample(200000)
print(f"R21 = {R21}")
#R21.generate_plot()

R22_ = 4e-3  # Ohm
delta_a_R22_ = (1 * R22_) / 100  # Ohm
R22 = mcpy.Rectangular(R22_, delta_a_R22_)
print(f"R22 = {R22}")
#R22.plot(N)

R3_ = 10e3  # Ohm
delta_a_R3_ = (5e-3 * R3_) / 100  # Ohm
R3 = mcpy.Rectangular(R3_, delta_a_R3_)
print(f"R3 = {R3}")
#R3.plot(N)

R4_ = 10e3
delta_R4_ = 0.5
R4 = mcpy.Rectangular(R4_, delta_R4_)
print(f"R4 = {R4}")
#R4.plot(N)

measurements = pd.read_csv("./examples/VoltageMeasurements.csv", sep=',', names=['u0', 'uh'])

U0_mean = mcpy.DirectObservations(measurements['u0'])
print(f"U0_mean = {U0_mean}")
#U0_mean.plot(N)


UH_mean = mcpy.DirectObservations(measurements['uh'])
print(f"UH_mean = {UH_mean}")
#UH_mean.plot(N)

U01_ = 100e-3  # Ohm
delta_a_U01_ = (40e-3 * float(U0_mean) + 20e-3 * U01_) / 100  # Ohm
U01 = mcpy.Rectangular(0, delta_a_U01_)
print(f"U01 = {U01}")
#U01.plot(N)

U02_ = 100e-3  # Ohm
delta_a_U02_ = (10e-6 / 2)  # Ohm
U02 = mcpy.Rectangular(0, delta_a_U02_)
print(f"U02 = {U02}")
#U02.plot(N)

UH1_ = 1
delta_a_UH1_ = (30e-3 * float(U0_mean) + 10e-3 * UH1_) / 100  # Ohm
UH1 = mcpy.Rectangular(0, delta_a_UH1_)
print(f"UH1 = {UH1}")
#UH1.plot(N)

UH2_ = 100e-3  # Ohm
delta_a_UH2_ = (100e-6 / 2)  # Ohm
UH2 = mcpy.Rectangular(0, delta_a_UH2_)
print(f"UH2 = {UH2}")
#UH2.plot(N)

delta_R1 = mcpy.Rectangular(0, 6.7e-3)
print(f"delta_R1 = {delta_R1}")
#delta_R1.plot(N)

uexp = ((40e-3 * 19e-3) / 100)
u_delta_theta = mcpy.Normal(6.7e-3, uexp, 3)
print(f"u_delta_theta = {u_delta_theta}")
#u_delta_theta.plot(N)

# ======================================================================================================================

RZ = mcpy.Uncertainty(105e-3)
print(f"RZ = {RZ}")
#RZ.plot(N)

R2: MCSamples = R21.mc_sample(N) + R22.mc_sample(N)
print(f"R2 = {R2}")
#R2.plot(N)

#R3.plot(N)
print(f"R3 = {R3}")

#R4.plot(N)
print(f"R4 = {R4}")

UH: MCSamples = UH_mean.mc_sample(N) - UH1.mc_sample(N) - UH2.mc_sample(N)
print(f"UH = {UH}")
# UH_mean.plot(N)
# UH1.plot(N)
# UH2.plot(N)
#UH.plot(N)

U0 = U0_mean.mc_sample(N) - U01.mc_sample(N) - U02.mc_sample(N)
print(f"U0 = {U0}")
# U0_mean.plot(N)
# U01.plot(N)
# U02.plot(N)
#U0.plot(N)

RL = 42e-3#mcpy.Uncertainty(42e-3)
print(f"RL = {RL}")
R1: MCSamples = (R2 + RZ.mc_sample(N)) * ((UH.rand(N) * (R3.mc_sample(N) + RZ.mc_sample(N)) - U0.mc_sample(N) *
                                           (R3.mc_sample(N) + R4.mc_sample(N) + 2 * RZ.mc_sample(N))) /
                                          (U0.mc_sample(N) * (R3.mc_sample(N) + R4.mc_sample(N) + 2 * RZ.mc_sample(N))
                                           + UH.rand(N) * (R4.mc_sample(N) + RZ.mc_sample(N)))) \
                - RL - RZ.mc_sample(N) + delta_R1.mc_sample(N)
print(f"R1 = {float(R1)} {R1.std}")
R1.plot(N)

R1 = (float(R2) + float(RZ)) * (
        (float(UH) * (float(R3) + float(RZ)) - float(U0) * (float(R3) + float(R4) + float(RZ) * 2))
        /
        (float(U0) * (float(R3) + float(R4) + float(RZ) * 2) + float(UH) * (float(R4) + float(RZ)))
) - float(RL) - float(RZ) + float(delta_R1)

print(f"R1 = {R1}")
R1.plot(N)