from twilio.rest import Client
import argparse
import re
import time

class Noice():
    def __init__(self,sid,auth_token,from_number):
        '''
        These are variables from your twilio.com account.
        
        Yes. You need to buy credit from them.

        '''
        self.sid = sid
        self.auth_token = auth_token
        self.from_number = from_number
        # an SMS client
        self.client = Client(self.sid, self.auth_token)

    @staticmethod
    def format_number(number):
        if not number.startswith('+1'):
            number = '+1' + number 
        if len(number) != 12:
            raise ValueError(f'{number} doesnt look like a phone number')
        return number

    def send_message(self,to_number,message=None):
        if message == None:
            message='The squeaky wheel gets the grease!'
        message = self.client.messages.create(
            to_number,
            from_=self.from_number,
            body=message
        )
        return message.sid

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=(
       "  /\/\ (_)_ __  _ __   ___  ___  ___ | |_ __ _    /\ \ \___ (_) ___ ___  \n"
       " /    \| | '_ \| '_ \ / _ \/ __|/ _ \| __/ _` |  /  \/ / _ \| |/ __/ _ \ \n"
       "/ /\/\ \ | | | | | | |  __/\__ \ (_) | || (_| | / /\  / (_) | | (_|  __/ \n"
       "\/    \/_|_| |_|_| |_|\___||___/\___/ \__\__,_| \_\ \/ \___/|_|\___\___| \n"                                                                     
       "Dont be a jerk.\n"),
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        '--sid',
        help='Twilio.com SID'
    )
    parser.add_argument(
        '--auth-token',
        help='Twilio.com auth token'
    )
    parser.add_argument(
        '--to-number',
        help='Your collaborators number'
    )
    parser.add_argument(
        '--from-number',
        help='One of your purchased Twilio.com numbers'
    )
    parser.add_argument(
        '--frequency',
        help='The starting frequency for each SMS message',
        type=int,
        default=60
    )
    parser.add_argument(
        '--nice-decay',
        default=10,
        type=int,
        help='After these many messages, the frequency will be halved.'
    )
    parser.add_argument(
        '--message',
        type=str,
        default=None
    )
    parser.add_argument(
        '--I_UNDERSTAND_DOS_ATTACKS_ARE_PROBABLY_ILLEGAL_WHERE_LIVE_AND_I_WAIVE_ALL_LIABILITY_FROM_THE_AUTHOR_OF_THIS_SOFTWARE',
        action='store_true'
    )

    args = parser.parse_args()
    x = Noice(args.sid,args.auth_token,args.from_number)
    sent = 0

    while True:
        if args.I_UNDERSTAND_DOS_ATTACKS_ARE_PROBABLY_ILLEGAL_WHERE_LIVE_AND_I_WAIVE_ALL_LIABILITY_FROM_THE_AUTHOR_OF_THIS_SOFTWARE:
            x.send_message(args.to_number,args.message)
            # Every 10 messages half the frequency until it is 1/sec (maniac!)
            if (sent % args.nice_decay == 0) and sent > 0 and args.frequency >= 1:
                args.frequency = max(1,args.frequency // 2)
            sent += 1
        print(f'Message: {args.message} sent! Waiting {args.frequency} seconds to try again.')
        time.sleep(args.frequency)
