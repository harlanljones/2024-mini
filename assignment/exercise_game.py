"""
Response time - single-threaded
"""

from machine import Pin
import time
import random
import json
import network
import urequests

wifi = network.WLAN(network.STA_IF)

N: int = 10
sample_ms = 10.0
on_ms = 500


def random_time_interval(tmin: float, tmax: float) -> float:
    """return a random time interval between max and min"""
    return random.uniform(tmin, tmax)


def blinker(N: int, led: Pin) -> None:
    # %% let user know game started / is over

    for _ in range(N):
        led.high()
        time.sleep(0.1)
        led.low()
        time.sleep(0.1)


def write_json(json_filename: str, data: dict) -> None:
    """Writes data to a JSON file.

    Parameters
    ----------

    json_filename: str
        The name of the file to write to. This will overwrite any existing file.

    data: dict
        Dictionary data to write to the file.
    """

    with open(json_filename, "w") as f:
        json.dump(data, f)


def scorer(t: list[int | None]) -> None:
    # %% collate results
    misses = t.count(None)
    print(f"You missed the light {misses} / {len(t)} times")

    t_good = [x for x in t if x is not None]

    print(t_good)

    # add key, value to this dict to store the minimum, maximum, average response time
    # and score (non-misses / total flashes) i.e. the score a floating point number
    # is in range [0..1]
    data = {}
    data['min_time'] = min(t_good)
    data['max_time'] = max(t_good)
    data['avg_time'] = sum(t_good) / len(t_good)
    data['score'] = len(t_good) / len(t)

    # %% make dynamic filename and write JSON

    now: tuple[int] = time.localtime()

    now_str = "-".join(map(str, now[:3])) + "T" + "_".join(map(str, now[3:6]))
    filename = f"score-{now_str}.json"
    
    print("write", filename)

    write_json(filename, data)
    
    if wifi.isconnected():
        print("Connected to wifi with IP address ", wifi.ifconfig()[0])
    else:
        print("Not connected to Wi-Fi")
        exit()
    
    FIRESTORE_URL = "https://firestore.googleapis.com/v1/projects/senior-design-mini-2/databases/(default)/documents/scores"
    post_data = {
        "fields": {
            "average_response_time": {"doubleValue": data['avg_time']},
            "minimum_response_time": {"doubleValue": data['min_time']},
            "maximum_response_time": {"doubleValue": data['max_time']}
        }
    }

    response = urequests.post(FIRESTORE_URL, json=post_data)
    print("FIRESTORE response:\n", response.text)
    response.close()

if __name__ == "__main__":
    # using "if __name__" allows us to reuse functions in other script files
    
    wifi.active(True)
    wifi.connect('BU Guest (unencrypted)')

    led = Pin("LED", Pin.OUT)
    button = Pin(16, Pin.IN, Pin.PULL_UP)

    t: list[int | None] = []

    blinker(3, led)

    for i in range(N):
        time.sleep(random_time_interval(0.5, 5.0))

        led.high()

        tic = time.ticks_ms()
        t0 = None
        while time.ticks_diff(time.ticks_ms(), tic) < on_ms:
            if button.value() == 0:
                t0 = time.ticks_diff(time.ticks_ms(), tic)
                led.low()
                break
        print(t0)
        t.append(t0)

        led.low()

    blinker(5, led)

    scorer(t)
