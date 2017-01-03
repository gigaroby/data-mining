./run.sh -graph ./graphs/3elt.graph -acceptanceFunction SIMPLE -alpha 2 -delta 0.03 -temp 2 -restartAfter -1 > /dev/null &
./run.sh -graph ./graphs/3elt.graph -acceptanceFunction SIMPLE -alpha 2 -delta 0.03 -temp 2 -restartAfter 600 > /dev/null &
./run.sh -graph ./graphs/add20.graph -acceptanceFunction SIMPLE -alpha 2 -delta 0.03 -temp 2 -restartAfter -1 > /dev/null &
./run.sh -graph ./graphs/add20.graph -acceptanceFunction SIMPLE -alpha 2 -delta 0.03 -temp 2 -restartAfter 600 > /dev/null &
./run.sh -graph ./graphs/facebook.graph -acceptanceFunction SIMPLE -alpha 2 -delta 0.03 -temp 2 -restartAfter -1 > /dev/null &
./run.sh -graph ./graphs/facebook.graph -acceptanceFunction SIMPLE -alpha 2 -delta 0.03 -temp 2 -restartAfter 600 > /dev/null &
./run.sh -graph ./graphs/twitter.graph -acceptanceFunction SIMPLE -alpha 2 -delta 0.03 -temp 2 -restartAfter -1 > /dev/null &
./run.sh -graph ./graphs/twitter.graph -acceptanceFunction SIMPLE -alpha 2 -delta 0.03 -temp 2 -restartAfter 600 > /dev/null &
./run.sh -graph ./graphs/3elt.graph -acceptanceFunction EXPONENTIAL -alpha 2 -delta 0.9 -temp 1 -restartAfter -1 > /dev/null &
./run.sh -graph ./graphs/3elt.graph -acceptanceFunction EXPONENTIAL -alpha 2 -delta 0.9 -temp 1 -restartAfter 600 > /dev/null &
./run.sh -graph ./graphs/add20.graph -acceptanceFunction EXPONENTIAL -alpha 2 -delta 0.9 -temp 1 -restartAfter -1 > /dev/null &
./run.sh -graph ./graphs/add20.graph -acceptanceFunction EXPONENTIAL -alpha 2 -delta 0.9 -temp 1 -restartAfter 600 > /dev/null &
./run.sh -graph ./graphs/facebook.graph -acceptanceFunction EXPONENTIAL -alpha 2 -delta 0.9 -temp 1 -restartAfter -1 > /dev/null &
./run.sh -graph ./graphs/facebook.graph -acceptanceFunction EXPONENTIAL -alpha 2 -delta 0.9 -temp 1 -restartAfter 600 > /dev/null &
./run.sh -graph ./graphs/twitter.graph -acceptanceFunction EXPONENTIAL -alpha 2 -delta 0.9 -temp 1 -restartAfter -1 > /dev/null &
./run.sh -graph ./graphs/twitter.graph -acceptanceFunction EXPONENTIAL -alpha 2 -delta 0.9 -temp 1 -restartAfter 600 > /dev/null &
wait
find output -name "*.txt" -exec ./plot.sh {} \;
