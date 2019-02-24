
from django import forms

class ConfigForm(forms.Form):
    mode = forms.ChoiceField(choices=[('0', '0'), ('1', '1')], label='Mode', required=True)
    coin_count = forms.IntegerField(max_value=50, min_value=1, label='Coin Count', required=True)
    game_count = forms.IntegerField(max_value=5, min_value=1, label='Game Count', required=True)
    game_time = forms.IntegerField(min_value=10, max_value=999, label='Game Time', required=True)
    music_volume = forms.IntegerField(min_value=0, max_value=100, label="Music Volume", required=True)
    sound_volume = forms.IntegerField(min_value=0, max_value=100, label='Sound Volume', required=True)
    resolution = forms.CharField(label='Resolution', required=True)
    spare_1 = forms.CharField(label='spare_1')
    spare_2 = forms.CharField(label='spare_2')
    spare_3 = forms.CharField(label='spare_3')
    spare_4 = forms.CharField(label='spare_4')
    spare_5 = forms.CharField(label='spare_5')