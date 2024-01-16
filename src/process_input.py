def extract_inputs(input: dict) -> dict:
    make_audio = input['make_audio']
    remove_new_lines = input["make_it_single"]
    lang_requested = input["lang_to_be_used"]

    return(make_audio, remove_new_lines, lang_requested)