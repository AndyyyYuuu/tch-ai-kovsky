import torch, music21
device = torch.device("cpu")

def get_notes_list_from_stream(midi_stream):
    note_filter = music21.stream.filters.ClassFilter('Note')
    stream_notes = []
    for note in midi_stream.recurse().addFilter(note_filter):
        note_dict = {
            'nameWithOctave': note.nameWithOctave,
            'fullName': note.fullName,
            'word': '{}_{}_{}'.format(note.pitch.name, str(note.pitch.octave), str(note.duration.type)).lower(),
            'pitch': {
                'name': note.pitch.name,
                'microtone': str(note.pitch.microtone),
                'octave': str(note.pitch.octave),
                'step': str(note.pitch.step)
            },
            'duration':{
                'type': str(note.duration.type)
            }
        }
        stream_notes.append(note_dict)
    return stream_notes

