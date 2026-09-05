# PBGen: Paper Base Generation Based on Writing Structure.

The code is the implementation of PBGen.



## Usage


Train the model:

`sh start.sh`



## Dataset

- data.json: The log data is organized in the structure:

`{"user_id": user_id, "log_num": log_num, "logs": [log1, log2, ...]]}`

`log = {"item_id": item_id, "score": score, "field_code": [field_code1, field_code2, ...], "tag": tag, "member": [member1, member2, ...]}`

- facv2vec.json: The case descriptions are encoded by BERT, organized as following structure：

`{"item_id": case_descriptions}`

To run the code, please place the downloaded dataset under the `data` folder.
