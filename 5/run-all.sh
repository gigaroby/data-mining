./run.sh -acceptanceFunction SIMPLE -rounds 1000 -alpha 2 -delta 0.003 -temp 2 -restartAfter -1
./run.sh -acceptanceFunction SIMPLE -rounds 1000 -alpha 2 -delta 0.03 -temp 2 -restartAfter -1
./run.sh -acceptanceFunction SIMPLE -rounds 1000 -alpha 2 -delta 0.0003 -temp 2 -restartAfter -1
./run.sh -acceptanceFunction SIMPLE -rounds 1000 -alpha 2 -delta 0.003 -temp 2 -restartAfter 400
./run.sh -acceptanceFunction SIMPLE -rounds 1000 -alpha 2 -delta 0.03 -temp 2 -restartAfter 400
./run.sh -acceptanceFunction SIMPLE -rounds 1000 -alpha 2 -delta 0.0003 -temp 2 -restartAfter 400
./run.sh -acceptanceFunction SIMPLE -rounds 1000 -alpha 2 -delta 0.003 -temp 2 -restartAfter 600
./run.sh -acceptanceFunction SIMPLE -rounds 1000 -alpha 2 -delta 0.03 -temp 2 -restartAfter 600
./run.sh -acceptanceFunction SIMPLE -rounds 1000 -alpha 2 -delta 0.0003 -temp 2 -restartAfter 600
./run.sh -acceptanceFunction EXPONENTIAL -rounds 1000 -alpha 2 -delta 0.9 -temp 1 -restartAfter -1
./run.sh -acceptanceFunction EXPONENTIAL -rounds 1000 -alpha 2 -delta 0.8 -temp 1 -restartAfter -1
./run.sh -acceptanceFunction EXPONENTIAL -rounds 1000 -alpha 2 -delta 0.99 -temp 1 -restartAfter -1
./run.sh -acceptanceFunction EXPONENTIAL -rounds 1000 -alpha 2 -delta 0.9 -temp 1 -restartAfter 400
./run.sh -acceptanceFunction EXPONENTIAL -rounds 1000 -alpha 2 -delta 0.8 -temp 1 -restartAfter 400
./run.sh -acceptanceFunction EXPONENTIAL -rounds 1000 -alpha 2 -delta 0.99 -temp 1 -restartAfter 400
./run.sh -acceptanceFunction EXPONENTIAL -rounds 1000 -alpha 2 -delta 0.9 -temp 1 -restartAfter 600
./run.sh -acceptanceFunction EXPONENTIAL -rounds 1000 -alpha 2 -delta 0.8 -temp 1 -restartAfter 600
./run.sh -acceptanceFunction EXPONENTIAL -rounds 1000 -alpha 2 -delta 0.99 -temp 1 -restartAfter 600

find output -name "*.txt" -exec ./plot.sh {} \;
