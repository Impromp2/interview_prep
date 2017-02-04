# Write a function condense_meeting_times() that takes an array of meeting time ranges and returns an array of condensed ranges.

"""
cases
	- end time after start time of another meeting
	- end time equal to start time of another meeting
	- end time before start time of another meeting

"""

# meeting_times = [ [0, 1], [3, 5], [4, 8], [10, 12], [9, 10] ]
meeting_times = [ [1, 10], [2, 6], [3, 5], [7, 9] ]

# return   [ [0, 1], [3, 8], [9, 12] ]

def condense_meeting_times(meeting_times):
	condensed_ranges = []

	for meeting in meeting_times:
		if not condensed_ranges:
			condensed_ranges.append([meeting[0], meeting[1]])
			continue
		
		curr_start = meeting[0]
		curr_end = meeting[1]

		for i in range(len(condensed_ranges)):
			check_start = condensed_ranges[i][0]
			check_end = condensed_ranges[i][1]

			# start time > end time of other meeting
			if curr_end < check_start:
				condensed_ranges.insert(i, meeting)
			elif curr_start > check_end:
				if i == len(condensed_ranges) - 1:
					condensed_ranges.append(meeting)
			elif curr_start > check_start and curr_end > check_end:
				condensed_ranges[i] = (check_start, curr_end)
			elif curr_start < check_start and curr_end < check_end:
				condensed_ranges[i] = (curr_start, check_end)
			elif curr_start < check_start and curr_end > check_end:
				condensed_ranges[i] = meeting

	print(condensed_ranges)
	return condensed_ranges


condense_meeting_times(meeting_times)