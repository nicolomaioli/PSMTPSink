import os
import errno
from datetime import datetime
from smtpd import SMTPServer


class SMTPSink(SMTPServer):

    no = 0
    dir_name = "SMTPSink"
    destination = None

    def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):
        print(f"\nIncoming transmission")
        print(f"from: {mailfrom}")
        print(f"to: {rcpttos}")

        now = datetime.now().strftime('%Y%m%d%H%M%S')
        filename = f"{now}-{self.no}.eml"
        file = os.path.join(self.destination, filename).__str__()

        with open(file, 'w', encoding='utf-8') as f:
            f.write(data.decode("utf-8"))

        print(f"{file}")

        self.no += 1

    def find_or_create_destination(self):
        home = os.path.expanduser("~")
        destination = os.path.join(home, self.dir_name)

        if not os.path.isdir(destination):
            print(f"Attempting to create destination directory '{destination}'")
            try:
                os.makedirs(destination)
                print(f"Created destination directory '{destination}'")
            except OSError as e:
                # using errno for cross-platform compatibility
                if e.errno != errno.EEXIST:
                    raise

        self.destination = destination
        print(f"Emails will be saved at {destination}")
