#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
brain_inertial = Inertial()
left_motor_a = Motor(Ports.PORT1, 1, False)
left_motor_b = Motor(Ports.PORT2, 1, False)
left_drive_smart = MotorGroup(left_motor_a, left_motor_b)

right_motor_a = Motor(Ports.PORT11, 1, True)
right_motor_b = Motor(Ports.PORT12, 1, True)
right_drive_smart = MotorGroup(right_motor_a, right_motor_b)
drivetrain_gyro = Gyro(Ports.PORT4)
drivetrain = SmartDrive(left_drive_smart, right_drive_smart, drivetrain_gyro, 200)
touchled_3 = Touchled(Ports.PORT3)
clawMotor = Motor(Ports.PORT7, False)
armMotor = Motor(Ports.PORT5, False)


def calibrate_drivetrain():
    # Calibrate the Drivetrain Gyro
    sleep(200, MSEC)
    brain.screen.print("Calibrating")
    brain.screen.next_row()
    brain.screen.print("Gyro")
    drivetrain_gyro.calibrate(GyroCalibrationType.NORMAL)
    while drivetrain_gyro.is_calibrating():
        sleep(25, MSEC)
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)


#endregion VEXcode Generated Robot Configuration
myVariable = 0

def when_started1():
    global myVariable
    touchled_3.set_color(Color.RED)
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 24, INCHES)
    drivetrain.turn_for(LEFT, 90, DEGREES)
    clawMotor.spin(FORWARD)
    # Prepare to Grab
    drivetrain.drive_for(FORWARD, 8, INCHES)
    clawMotor.spin(REVERSE)
    # Grabs 1st block
    wait(1, SECONDS)
    armMotor.spin_for(FORWARD, 1, TURNS)
    touchled_3.set_color(Color.GREEN)
    drivetrain.drive_for(FORWARD, 42, INCHES)
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 18, INCHES)
    armMotor.spin_for(REVERSE, 1, TURNS)
    clawMotor.set_timeout(1, SECONDS)
    clawMotor.spin(FORWARD)
    # Drop off the 1st block
    armMotor.spin_for(FORWARD, 2, TURNS)
    touchled_3.set_color(Color.RED)
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 11, INCHES)
    drivetrain.turn_for(LEFT, 90, DEGREES)
    brain.play_sound(SoundType.WRONG_WAY)
    drivetrain.drive_for(REVERSE, 29, INCHES)
    brain.play_sound(SoundType.WRONG_WAY)
    # Plays sound before and after reverse driving
    # Reversing toward 2nd block
    drivetrain.turn_for(RIGHT, 180, DEGREES)
    armMotor.spin_for(REVERSE, 2, TURNS)
    drivetrain.drive_for(FORWARD, 7, INCHES)
    clawMotor.spin(REVERSE)
    # Grabs 2nd block
    wait(1, SECONDS)
    armMotor.spin_for(FORWARD, 1, TURNS)
    touchled_3.set_color(Color.GREEN)
    # Grabs 2nd block
    drivetrain.turn_for(RIGHT, 180, DEGREES)
    drivetrain.drive_for(FORWARD, 45, INCHES)
    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 2, INCHES)
    armMotor.spin_for(REVERSE, 1, TURNS)
    clawMotor.set_timeout(1, SECONDS)
    clawMotor.spin(FORWARD)
    armMotor.spin_for(FORWARD, 2, TURNS)
    # Drops off 2nd block
    touchled_3.set_color(Color.RED)
    drivetrain.turn_for(RIGHT, 180, DEGREES)
    armMotor.spin_for(REVERSE, 2, TURNS)
    drivetrain.drive_for(FORWARD, 21, INCHES)
    clawMotor.spin(REVERSE)
    # Grabs 3rd block
    wait(1, SECONDS)
    armMotor.spin_for(FORWARD, 2, TURNS)
    touchled_3.set_color(Color.GREEN)
    drivetrain.turn_for(RIGHT, 180, DEGREES)
    drivetrain.drive_for(FORWARD, 19, INCHES)
    armMotor.spin_for(REVERSE, 2, TURNS)
    clawMotor.set_timeout(1, SECONDS)
    clawMotor.spin(FORWARD)
    # Drops 3rd block
    armMotor.spin_for(FORWARD, 2, TURNS)
    touchled_3.set_color(Color.PURPLE)
    brain.play_sound(SoundType.TADA)

# Calibrate the Drivetrain Gyro
calibrate_drivetrain()

when_started1()
