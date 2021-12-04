class Text:
    how_to = "`Ya bir ses dosyasına yanıt verin ya da bana oynatmam için bir youtube bağlantısı verin!`"
    not_yet = "`Bu henüz desteklenmiyor!"
    dl = "`İndiriliyor...`"
    helper = """
**Kullanılabilir Komutlar:**\n
  - `{x}alive` - __Botun çevrimiçi olup olmadığını kontrol edin.__
  - `{x}oynat <url/şarkı dosyasına yanıt ver>` - __Sesli Sohbet'de şarkı çal.__ 
  - `{x}durdur` - __parçayı duraklat.__
  - `{x}devam` - __duraklatılmış parçayı devam ettirir.__
  - `{x}indir <şarkı adı>` - __şarkı indir__

**Support:** __@PyhsicalBeing__."""


async def play_a_song(pycalls, message, song):
    try:
        await pycalls.stream(message.chat.id, song)
    except Exception as e:
        await message.reply_text(f"HATA:\n{e}")
