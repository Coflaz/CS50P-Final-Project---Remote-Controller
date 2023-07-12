import time

class RemoteController:
    def __init__(self, on_off="On", channels=["A-Haber", "SZC", "TRT"], channel_now="SZC", volume=70, brightness=8):
        time.sleep(1)
        self.on_off = on_off
        self.channels = channels
        self.channel_now = channel_now
        self.volume = volume
        self.brightness = brightness

    def tv_status(self):
        time.sleep(1)
        return f"""
        TV is {self.on_off}
        You are watching {self.channel_now}
        The volume is at {self.volume} level
        The brightness is at {self.brightness} level
        """

    def on_off_main(self):
        if self.on_off == "On":
            time.sleep(1)
            self.on_off = "Off"
            return "TV is Off"
        elif self.on_off == "Off":
            time.sleep(1)
            self.on_off = "On"
            return "TV is On"
        else:
            pass

    def add_channel(self, channel_name):
        time.sleep(1)
        if not len(self.channels) <= 0:
            self.channels.append(channel_name)
            return f"{channel_name} is added"

    def delete_channel(self, channel):
        if channel in self.channels:
            self.channels.remove(channel)
            time.sleep(1)
            return f"Channel {channel} is deleted"
        else:
            time.sleep(1)
            return "Couldn't find the channel"

    def see_channels(self):
        time.sleep(1)
        result = "Your Channels\n"
        for i, channel in enumerate(self.channels):
            time.sleep(1)
            result += f"Channel {i + 1}: {channel}\n"
        return result

    def channel_choose(self, channel_number):
        time.sleep(1)
        if channel_number <= len(self.channels) and channel_number > 0:
            self.channel_now = self.channels[channel_number - 1]
            return f"{self.channel_now} is streaming"

    def change_brightness(self, change):
        if change == "+":
            self.brightness += 1
            return f"Brightness: {self.brightness}"
        elif change == "-":
            self.brightness -= 1
            return f"Brightness: {self.brightness}"
        else:
            return f"Brightness: {self.brightness}"

    def change_volume(self, change):
        result = f"Volume: {self.volume}\n"
        if change[0] == "+":
            try:
                if len(change) == 2:
                    change_value = int(change[1])
                elif len(change) == 3:
                    change_value = int(change[1:3])
                if change_value + self.volume <= 100:
                    self.volume += change_value
                    result += f"Volume: {self.volume}"
                    return result
                else:
                    return "Enter a smaller amount"
            except:
                return "Unknown Input"
        elif change[0] == "-":
            try:
                if len(change) == 2:
                    change_value = int(change[1])
                elif len(change) == 3:
                    change_value = int(change[1:3])
                if self.volume - change_value >= 0:
                    self.volume -= change_value
                    result += f"Volume: {self.volume}"
                    return result
                else:
                    return "Enter a bigger amount"
            except:
                return "Unknown Input"

def main():
    remote = RemoteController()

    functions_list = """
        1 to see the status of your TV
        2 to turn on/off the TV
        3 to see your channel list
        4 to add channel
        5 to delete channel
        6 to choose a channel
        7 to change brightness
        8 to change volume
        9 to repeat the functions list
        0 to quit
        """
    print(functions_list)

    while True:
        function = input("\nWhat do you want to do? \n")

        if function == "0":
            print("Goodbye!")
            break
        elif function == "1":
            print(remote.tv_status())
        elif function == "2":
            print(remote.on_off_main())
        elif function == "3":
            print(remote.see_channels())
        elif function == "4":
            channel = input("What channel do you want to add? ")
            if channel == "" or channel == " ":
                print("Unknown input")
            elif channel not in remote.channels:
                print(remote.add_channel(channel))
            else:
                print("That channel is already in your list")
        elif function == "5":
            channel = input("What channel do you want to delete? ")
            print(remote.delete_channel(channel))
        elif function == "6":
            try:
                channel_number = int(input("Which channel do you want to watch? \n(enter the desired channel's number please)"))
                if channel_number in range(1, len(remote.channels) + 1):
                    print(remote.channel_choose(channel_number))
                else:
                    print("Not in your channel list")
            except ValueError as e:
                print("Invalid input: {}".format(e))
        elif function == "7":
            change = input(
                """
                Brightness Up: '+'
                Brightness Down: '-'
                Quit: 'Q' or 'q'
                """
            )
            print(remote.change_brightness(change))
        elif function == "8":
            change = input(
                """
                Increase By: 
                Decrease By:
                Quit: 'Q' or 'q'
                """
            )
            print(remote.change_volume(change))
        elif function == "9":
            print(functions_list)
        else:
            print("Unknown Function")

if __name__ == "__main__":
    main()


    