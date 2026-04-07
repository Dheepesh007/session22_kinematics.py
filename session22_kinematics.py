# SESSION 22 – AMAZON (Kinematics)

def determine_motion(left_wheel, right_wheel):
    if left_wheel == right_wheel:
        return "Straight Line Motion"
    else:
        return "Turning Motion"

def main():
    left_wheel = 3
    right_wheel = 3

    motion = determine_motion(left_wheel, right_wheel)

    print("Left Wheel Speed:", left_wheel)
    print("Right Wheel Speed:", right_wheel)
    print("Motion:", motion)

if __name__ == "__main__":
    main()
