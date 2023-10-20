# media.py
import winsdk.windows.media.control
import asyncio
import json
async def get_media_info():
    session_manager = await winsdk.windows.media.control.GlobalSystemMediaTransportControlsSessionManager.request_async()
    current_session = session_manager.get_current_session()
    if current_session:
        media_properties = await current_session.try_get_media_properties_async()
        playback_properties = current_session.get_playback_info()
        if playback_properties.playback_status != winsdk.windows.media.control.GlobalSystemMediaTransportControlsSessionPlaybackStatus.PAUSED:
            media_playback_info = {
                "titleAndArtist": media_properties.title + " - " + media_properties.artist
            }
            print(json.dumps(media_playback_info))
            return

    media_playback_info = {
        "titleAndArtist": ""
    }
    print(json.dumps(media_playback_info))

asyncio.run(get_media_info())