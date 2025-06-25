class PIDController:
    def __init__(self, Kp, Ki, Kd):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.integral = 0
        self.prev_error = 0

    def update(self, error):
        self.integral += error
        derivative = error - self.prev_error
        self.prev_error = error

        output = (
            # Kp * error = correct the error proportional to the size of the error - how far should the mirror move
            self.Kp * error +
            # Ki * integral = Addressing long-term errors, if the error is still persistent over time,increase 
            self.Ki * self.integral +
            # Kd * currentError-PrevError ; anticipating future by dampening the correction - braking when increasing too much
            self.Kd * derivative
        )
        return output


def applyPID(laser_x, laser_y):
    # Image parameters
    width, height = (640,480)
    targetX, targetY = width // 2, height // 2  # target center

    # # Initialize PID controllers
    pid_x = PIDController(Kp=0.3, Ki=0.01, Kd=0.05)
    pid_y = PIDController(Kp=0.3, Ki=0.01, Kd=0.05)

    # Store tracking error for plotting
    error_history = []

    for i in range(200):
        # Simulate detected position (you could add measurement noise here)
        detected_x = laser_x
        detected_y = laser_y

        # Calculate errors
        error_x = detected_x - targetX
        error_y = detected_y - targetY

        # Get PID correction
        correction_x = pid_x.update(error_x)
        correction_y = pid_y.update(error_y)

        # Apply correction — this simulates what the mirror would do
        laser_x -= correction_x
        laser_y -= correction_y

        # Record current distance from center
        distance = ((detected_x - targetX)**2 + (detected_y - targetY)**2)**0.5
        error_history.append(distance)

    return error_history, laser_x, laser_y


