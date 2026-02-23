class rsi:
    def __init__(self, period=14):
        self.period = period
        self.prev_price = None
        self.gains = []
        self.losses = []
        self.avg_gain = None
        self.avg_loss = None
        self.ready = False

    def update(self, price: float):
        if self.prev_price is None:
            self.prev_price = price
            return None  # not enough data

        change = price - self.prev_price
        self.prev_price = price

        gain = max(change, 0)
        loss = max(-change, 0)

        # Seeding phase
        if not self.ready:
            self.gains.append(gain)
            self.losses.append(loss)

            if len(self.gains) < self.period:
                return None  # still warming up

            # Seed with simple average
            self.avg_gain = sum(self.gains) / self.period
            self.avg_loss = sum(self.losses) / self.period
            self.ready = True
        else:
            # Wilder smoothing
            self.avg_gain = ((self.avg_gain * (self.period - 1)) + gain) / self.period
            self.avg_loss = ((self.avg_loss * (self.period - 1)) + loss) / self.period

        if self.avg_loss == 0:
            return 100.0

        value = 100 * self.avg_gain / (self.avg_gain + self.avg_loss)
        return value