class PID:
    def __init__(self, kp, ki, kd, setpoint=0, output_limits=(-100, 100)):
        self.kp = kp
        self.ki = ki
        self.kd = kd

        self.setpoint = setpoint
        self.output_limits = output_limits

        self._last_error = 0
        self._integral = 0

    def compute(self, current_value, dt):
        error = self.setpoint - current_value
        self._integral += error * dt
        derivative = (error - self._last_error) / dt if dt > 0 else 0

        output = (self.kp * error) + (self.ki * self._integral) + (self.kd * derivative)
        output = max(min(output, self.output_limits[1]), self.output_limits[0])

        self._last_error = error
        return output