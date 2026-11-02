# Mechanical Component Stress & Factor of Safety (FOS) Calculator

def calculate_stress(force, area):
    """Calculates stress in MPa (Force in N, Area in mm^2)"""
    if area <= 0:
        return 0
    return force / area

def check_safety_factor(yield_strength, actual_stress):
    """Calculates Factor of Safety (FOS)"""
    if actual_stress <= 0:
        return float('inf')
    return yield_strength / actual_stress

# Sample Material Data (Yield Strength in MPa)
materials = {
    "Structural Steel": 250,
    "Aluminum 6061-T6": 276,
    "Cast Iron (Gray)": 130
}

print("--- Mechanical Design Data Analyzer ---")
print("Available Materials:", list(materials.keys()))

# Inputs for simulation
force_input = 50000  # Force in Newtons (50 kN)
area_input = 250     # Cross-sectional area in mm^2

calculated_stress = calculate_stress(force_input, area_input)
print(f"\nCalculated Design Stress: {calculated_stress:.2f} MPa")

print("\n--- Safety Analysis Report ---")
for mat, yield_str in materials.items():
    fos = check_safety_factor(yield_str, calculated_stress)
    status = "SAFE" if fos >= 1.5 else "UNSAFE (Redesign Required)"
    print(f"Material: {mat} | Yield Strength: {yield_str} MPa | FOS: {fos:.2f} | Status: {status}")
