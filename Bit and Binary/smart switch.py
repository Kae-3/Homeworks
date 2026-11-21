class SmartSwitchMonitor:
    def __init__(self, num_switches: int = 8, initial_state: int = 0):
        self.num_switches = num_switches
        self._mask = (1 << num_switches) - 1
        self.state = initial_state & self._mask

    def turn_on(self, switch_idx: int):
        self._validate_index(switch_idx)
        self.state |= (1 << switch_idx)

    def turn_off(self, switch_idx: int):
        self._validate_index(switch_idx)
        self.state &= ~(1 << switch_idx)

    def toggle(self, switch_idx: int):
        self._validate_index(switch_idx)
        self.state ^= (1 << switch_idx)

    def is_on(self, switch_idx: int) -> bool:
        self._validate_index(switch_idx)
        return ((self.state >> switch_idx) & 1) == 1

    def active_switches(self):
        return [i for i in range(self.num_switches) if self.is_on(i)]

    def display_status(self):
        print(f"Switch Register: 0b{self.state:0{self.num_switches}b} (Decimal: {self.state})")
        for idx in range(self.num_switches - 1, -1, -1):
            status = "ON " if self.is_on(idx) else "OFF"
            print(f"  Switch {idx}: {status}")

    def _validate_index(self, switch_idx: int):
        if not (0 <= switch_idx < self.num_switches):
            raise ValueError(f"Switch index must be between 0 and {self.num_switches - 1}")


# Example usage
monitor = SmartSwitchMonitor(num_switches=6, initial_state=0b000101)
monitor.turn_on(3)      # Turn ON switch 3
monitor.turn_off(0)     # Turn OFF switch 0
monitor.toggle(5)       # Toggle switch 5 ON
monitor.display_status()
print("Switches currently ON:", monitor.active_switches())
print("Total ON count:", monitor.state.bit_count())