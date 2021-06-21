from django.forms import ModelForm, Textarea
from auctions.models import Listing, Bids


class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['item', 'description', 'startBid', 'imageURL', 'category']
        widgets = {
            'description': Textarea(attrs={'cols': 40, 'rows': 6}),
        }


class BidForm(ModelForm):
    class Meta:
        model = Bids
        fields = ['offer']