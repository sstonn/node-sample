import json
import asyncio
from bleak import BleakScanner

def contains(small, big):
    for i in range(len(big)-len(small)+1):
        for j in range(len(small)):
            if big[i+j] != small[j]:
                break
        else:
            return i, i+len(small)
    return False

async def run():
    devices = await BleakScanner.discover()

    realDevices = []
    for d in devices:
        metadata={'uuids': d.metadata['uuids']}
        for key in d.metadata["manufacturer_data"]:
            metadata["manufacturer_data"] = {key: memoryview(d.metadata["manufacturer_data"][key]).tolist()}
        realDevices.append({
                "id": str(devices.index(d)),
                "name": d.name,
                "address": d.address,
                "metadata": metadata
            })
    print(json.dumps(realDevices))
loop = asyncio.get_event_loop()
loop.run_until_complete(run())