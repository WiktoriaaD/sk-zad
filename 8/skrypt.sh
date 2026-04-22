#!/bin/bash

for Y in {71..90}; do
	if [ "$Y" -ne 88 ] && [ "$Y" -ne 89 ]; then
		sudo ip route add 10.192.$Y.0/30 via 192.168.48.$Y
	fi
done
