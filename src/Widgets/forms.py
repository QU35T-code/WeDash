from django import forms

class Shortener(forms.Form):
    shortener = forms.URLField(label="shortener", help_text="Enter an url", max_length=100, required=True)
    def clean(self):
        cleaned_data = super(Shortener, self).clean()
        name = cleaned_data.get('shortener')
        if not name:
            raise forms.ValidationError('You have to write something!')

class Hash(forms.Form):
    hash = forms.CharField(label="hash", help_text="Enter a hash", max_length=100, required=True)
    def clean(self):
        cleaned_data = super(Hash, self).clean()
        name = cleaned_data.get('hash')
        if not name:
            raise forms.ValidationError('You have to write something!')

CRYPTO_CHOICES =(
    ("BTC", "Bitcoin"),
    ("ETH", "Ethereum"),
    ("BNB", "BNB"),
    ("USDT", "Tether"),
    ("SOL", "Solana"),
    ("ADA", "Cardano"),
    ("USDC", "USD Coin"),
    ("XRP", "XRP"),
    ("DOT", "Polkadot"),
    ("DOGE", "Dogecoin"),
    ("LUNA", "Terra"),
    ("AVAX", "Avalanche"),
    ("SHIB", "Shiba Inu"),
    ("MATIC", "Polygon"),
    ("LTC", "Litecoin"),
    ("UNI", "Uniswap"),
    ("ALGO", "Algorand"),
)

class Crypto(forms.Form):
    crypto_choice = forms.ChoiceField(choices=CRYPTO_CHOICES, required=True)

HOROSCOPE_CHOICES =(
    ("ARIES", "Aries"),
    ("TAURUS", "Taurus"),
    ("GEMINI", "Gemini"),
    ("LEO", "Leo"),
    ("CANCER", "Cancer"),
    ("VIRGO", "Virgo"),
    ("LIBRA", "Libra"),
    ("SCORPIO", "Scorpio"),
    ("SAGITTARIUS", "Sagittarius"),
    ("CAPRICORNUS", "Capricornus"),
    ("AQUARIUS", "Aquarius"),
    ("PISCES", "Pisces"),
)

class Horoscope(forms.Form):
    horoscope_choice = forms.ChoiceField(choices=HOROSCOPE_CHOICES, required=True)

LANGS =(
    ("fr", "French"),
    ("en", "English"),
    ("ar", "Arabic"),
    ("de", "German"),
    ("es", "Spanish"),
    ("he", "Hebrew"),
    ("it", "Italian"),
    ("nl", "Dutch"),
    ("pt", "Portuguese"),
    ("ru", "Russian"),
    ("se", "Sami"),
    ("zh", "Chinese"),
)

class News(forms.Form):
    keyword_choice = forms.CharField(label="keyword", help_text="Enter a keyword", max_length=20, required=True)
    lang_choice = forms.ChoiceField(choices=LANGS, required=True)