# Dont be nice. Be Minnesota Nice
This script sends SMS messages from your Twilio account in the most passive aggressive way
possible. 

**Note:: At any time users can respond "STOP" to a SMS message and unsubscribe** 



# Usage
```
usage: PassiveAggressive.py [-h] [--sid SID] [--auth-token AUTH_TOKEN]
                            [--to-number TO_NUMBER]
                            [--from-number FROM_NUMBER]
                            [--frequency FREQUENCY] [--nice-decay NICE_DECAY]
                            [--message MESSAGE]
                            [--I_UNDERSTAND_DOS_ATTACKS_ARE_PROBABLY_ILLEGAL_WHERE_LIVE_AND_I_WAIVE_ALL_LIABILITY_FROM_THE_AUTHOR_OF_THIS_SOFTWARE]

  /\/\ (_)_ __  _ __   ___  ___  ___ | |_ __ _    /\ \ \___ (_) ___ ___  
 /    \| | '_ \| '_ \ / _ \/ __|/ _ \| __/ _` |  /  \/ / _ \| |/ __/ _ \ 
/ /\/\ \ | | | | | | |  __/\__ \ (_) | || (_| | / /\  / (_) | | (_|  __/ 
\/    \/_|_| |_|_| |_|\___||___/\___/ \__\__,_| \_\ \/ \___/|_|\___\___| 
Dont be a jerk.

optional arguments:
  -h, --help            show this help message and exit
  --sid SID             Twilio.com SID
  --auth-token AUTH_TOKEN
                        Twilio.com auth token
  --to-number TO_NUMBER
                        Your collaborators number
  --from-number FROM_NUMBER
                        One of your purchased Twilio.com numbers
  --frequency FREQUENCY
                        The starting frequency for each SMS message
  --nice-decay NICE_DECAY
                        After these many messages, the frequency will be
                        halved.
  --message MESSAGE
  --I_UNDERSTAND_DOS_ATTACKS_ARE_PROBABLY_ILLEGAL_WHERE_LIVE_AND_I_WAIVE_ALL_LIABILITY_FROM_THE_AUTHOR_OF_THIS_SOFTWARE
```

