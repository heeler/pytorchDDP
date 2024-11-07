#!/bin/sh

beaker session create --image beaker://"$(beaker account whoami --format json | jq -r .[].name)"/pytorch_dpp_1 --bare --budget ai2/reviz --gpus 2 --mount weka://ai1-default=/weka/ai1
