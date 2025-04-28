from gailbot import GailBot, ProfileSetting
gb = GailBot()
deepgram_api = "YOUR DEEPGRAM KEY HERE"
input = "parkinsons_audio.wav"
output = "output" # location of an output folder
gb.login("123", "asdf")

# can add more settings here
deepgram_engine_setting = {"engine": "deepgram", "deepgram_api_key": deepgram_api}

deepgram_engine_name = "deepgram"
print(gb.get_engine_setting("deepgram"))
deepgram_profile_setting = ProfileSetting(
    engine_setting_name=deepgram_engine_name,
    plugin_suite_setting={
       # "HiLabSuite": ["XmlPlugin", "ChatPlugin", "TextPlugin", "CSVPlugin"]
    }
)
deepgram_profile_name = "deepgram profile2"
gb.create_profile(name=deepgram_profile_name, setting=deepgram_profile_setting)
s1 = (input, output)
s2 = (input, output)
source_id = gb.add_source(input, output)
sources_id = gb.add_sources([s1, s2])
gb.apply_profile_to_source(source_id=source_id, profile_name=deepgram_profile_name)
google_transcription_result = gb.transcribe()
print(google_transcription_result)