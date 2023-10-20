# media.py
import winsdk.windows.media.control
import asyncio
import json
async def get_media_info():
    session_manager = await winsdk.windows.media.control.GlobalSystemMediaTransportControlsSessionManager.request_async()
    current_session = session_manager.get_current_session()
    media_properties = await current_session.try_get_media_properties_async()
    media_playback_info = {
        "title": media_properties.title,
        "artist": media_properties.artist,
        "album": media_properties.album_title,
        "album_artist": media_properties.album_artist,
        "track": media_properties.track_number
    }
    print(json.dumps(media_playback_info))
asyncio.run(get_media_info())