from .models import *
from decimal import Decimal
import re


def analyze(this_file_here):
    lines = this_file_here.readlines()
    mySet1 = set()
    mySet2 = set()

    for i, line in enumerate(lines):
        my_line = line.decode('UTF-8')
        can_id_match = re.search("ID = (\d+)", my_line)
        if can_id_match:
            can_id = int(can_id_match.group(1))
            channel_match = re.search(" (\d) ", my_line)
            channel = int(channel_match.group(1))
            if channel == 1:
                mySet1.add(can_id)
            if channel == 2:
                mySet2.add(can_id)

    mySet1 = sorted(mySet1)
    mySet2 = sorted(mySet2)

    return mySet1, mySet2


def update_database(file):
    print(file)
    #new_trace = Trace(name=file)
    #new_trace.save()

    can_channel_set = set()
    can_message_set_1 = set()
    can_message_set_2 = set()

    lines = file.readlines()
    for i, coded_line in enumerate(lines):
        line = coded_line.decode('UTF-8')
        regex = '(\d+\.\d+)\s+(\d)\s+(\w+)\s+Rx\s+d\s(\d)\s(.+)\s{2}Length.+ID = (\d+)'
        # line_match = re.search("Rx\s + d\s(\d)\s(. +)\s{2}Length", line)
        line_match = re.search(regex, line)
        if line_match:
            can_channel_set.add(int(line_match.group(2)))
            if line_match.group(2) == '1':
                #print(line_match.group(3))
                can_message_set_1.add(int(line_match.group(6)))
            if line_match.group(2) == '2':
                can_message_set_2.add(int(line_match.group(6)))
            #print("time=" + line_match.group(1))
            #print("channel=" + line_match.group(2))
            #print("hex id=" + line_match.group(3))
            #print("data_length=" + line_match.group(4))
            #print("data=" + line_match.group(5))

    can_channel_set = sorted(can_channel_set)
    print(can_channel_set)
    can_message_set_1 = sorted(can_message_set_1)
    print(can_message_set_1)
    can_message_set_2 = sorted(can_message_set_2)
    print(can_message_set_2)


def update_database2(file):
    trace_obj, trace_created = Trace.objects.get_or_create(name=file)
    if trace_created:
        lines = file.readlines()
        for i, coded_line in enumerate(lines):
            line = coded_line.decode('UTF-8')
            regex = '(\d+\.\d+)\s+(\d)\s+(\w+)\s+Rx\s+d\s(\d)\s(.+)\s{2}Length.+ID = (\d+)'
            line_match = re.search(regex, line)
            if line_match:
                channel = int(line_match.group(2))
                channel_obj, channel_obj_created = Channel.objects.get_or_create(trace=trace_obj,
                                                                                 canChannel=channel)
                message = int(line_match.group(6))
                message_obj, message_created = Message.objects.get_or_create(channel=channel_obj,
                                                                             can_id_decimal=message)

                frame_time = Decimal(line_match.group(1))
                data_length = int(line_match.group(4))
                frame_obj, frame_obj_created = Frame.objects.get_or_create(message=message_obj,
                                                                           time=frame_time,
                                                                           data_length=data_length)

                full_data = line_match.group(5)
                for byte in range(data_length):
                    start = byte*3
                    end = start+2
                    my_hex = full_data[start:end]
                    my_dec = int(my_hex, 16)
                    myData = Data(frame=frame_obj,
                                  byte_id=byte,
                                  hex_data=my_hex,
                                  dec_data=my_dec)
                    myData.save()






