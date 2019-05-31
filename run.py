# A simple SMTP sink based on this Django snippet
# https://www.djangosnippets.org/snippets/96/

import sys
import asyncore
from smtp_sink.SMTPSink import SMTPSink


def run():
    sink = SMTPSink(('localhost', 8000), None)
    sink.find_or_create_destination()

    try:
        print("Running SMTP server")
        asyncore.loop()
    except KeyboardInterrupt:
        print("\nBye!")
        sys.exit(0)


if __name__ == '__main__':
    run()
