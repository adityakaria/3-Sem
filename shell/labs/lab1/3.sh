#!/bin/bash
echo "enter basic pay"
read basic
dp=$(echo "scale=3; 0.5 * $basic"|bc);

da=$(echo "scale=3; 0.35 *($basic + $dp)"|bc)
hra=$(echo "scale=3; 0.08*($basic + $dp)"|bc)

ma=$(echo "scale=3; 0.03*($basic + $dp)"|bc)

pf=$(echo "scale=3; 0.1*($basic + $dp)"|bc)


salary=$(echo "scale=3; (($basic + $da + $dp + $hra + $ma) - $pf) "|bc)

echo $salary