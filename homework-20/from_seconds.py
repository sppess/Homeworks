def from_seconds(time):
    try:
        return int(time) * 60
    except ValueError:
        f_time = float(time)
        min_ = int(f_time) * 60
        sec = (f_time - int(f_time)) * 100
        time_sec = int(min_ + sec)
        return time_sec


assert (from_seconds('2')) == 120
assert (from_seconds('2.44')) == 164
assert (from_seconds('2.60')) == 180
assert (from_seconds('63.02')) == 3782
