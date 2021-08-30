#    Copyright 2021 Chase Kidder

#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

# main.py

import json

har_path = "D:\\backup\\class_materials\\ECET-37600\\Lecture 2 -\\cdnapisec.kaltura.com_Archive [21-08-30 13-49-17].har"

with open(har_path) as f:
    har = json.loads(f.read())

for req in har["log"]["entries"]:
    url = req["request"]["url"]
    print(url)

pass