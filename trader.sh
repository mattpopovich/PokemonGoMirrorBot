#!/bin/bash

### I first tried to make this script in bash, but quickly realized that if I wanted sufficient logic,
#   I should probably use a higher level language.

seed=12345

# Function to randomize the location with specified randomness range
randomize_location() {
  # Input: location in the form "x,y" and randomness range
  location=$1
  randomness=$2

  # Split the location into x and y coordinates
  IFS=',' read -r location_x location_y <<< "$location"

  # Generate random offsets between -randomness and +randomness for both x and y
  random_offset_x=$((RANDOM % (2 * randomness + 1) - randomness))  # Random value between -randomness and +randomness
  random_offset_y=$((RANDOM % (2 * randomness + 1) - randomness))  # Random value between -randomness and +randomness

  # Calculate the new coordinates by adding the offsets to the original location
  new_x=$((location_x + random_offset_x))
  new_y=$((location_y + random_offset_y))

  # Output the new randomized location
  echo "$new_x,$new_y"
}

# Function to sleep for a given time with randomness and return actual sleep time
random_sleep() {
  # Input: sleep time, randomness range
  base_sleep_time=$1
  randomness=$2

  # Increment the seed so that each call is different (but repeatable)
  seed=$(($seed+1))
  RANDOM=$seed

  # Generate a random offset in the range [-randomness, +randomness]
  offset=$(awk -v min=-$randomness -v max=$randomness -v seed=$seed \
                  'BEGIN{srand(seed); print min + rand() * (max - min)}')

  # Calculate the actual sleep time
  actual_sleep_time=$(awk -v sleep=$base_sleep_time -v offset=$offset \
                             'BEGIN{print sleep + offset}')

  # Ensure the sleep time is non-negative
  actual_sleep_time=$(awk -v time=$actual_sleep_time 'BEGIN{print (time < 0 ? 0 : time)}')

  # Sleep for the calculated time
  sleep $actual_sleep_time

  # Return the actual sleep time
  echo $actual_sleep_time
}

startTrade="3377,1285"
bottomCenterPokemon="3266,1321"
next="3268,1321"
confirm="3141,1086"
x="3268,1389"
randomness=10

# Activate window
cliclick c:$(randomize_location "$startTrade" "$randomness")


for i in {1..10}
do
  remaining_sleep=45.0
  # Start trading
  cliclick c:$(randomize_location "$startTrade" "$randomness")
  # sleep 3
  remaining_sleep=$(echo "$remaining_sleep - $(random_sleep 5.0 2.0)" | bc)
  echo "remaining sleep $remaining_sleep"
  cliclick c:$(randomize_location "$bottomCenterPokemon" "$randomness")
  # sleep 2
  remaining_sleep=$(echo "$remaining_sleep - $(random_sleep 4.0 2.0)" | bc)
  echo "remaining sleep $remaining_sleep"
  cliclick c:$(randomize_location "$next" "$randomness")
  # sleep 3
  remaining_sleep=$(echo "$remaining_sleep - $(random_sleep 5.0 2.0)" | bc)
  echo "remaining sleep $remaining_sleep"
  cliclick c:$(randomize_location "$confirm" "$randomness")
  # sleep 12
  remaining_sleep=$(echo "$remaining_sleep - $(random_sleep 14.0 2.0)" | bc)
  echo "remaining sleep $remaining_sleep"
  cliclick c:$(randomize_location "$x" "$randomness")
  # sleep 3
  remaining_sleep=$(echo "$remaining_sleep - $(random_sleep 5.0 2.0)" | bc)
  echo "remaining sleep $remaining_sleep"

  sleep $remaining_sleep
done
