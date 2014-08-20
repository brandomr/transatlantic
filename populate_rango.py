import os

def populate():
	
	Ebola_cat = add_cat('Ebola', 128, 64)
	
	add_page(cat=Ebola_cat,
		title="New, Larger Ebola Center Opens in Liberia",
		url="http://www.nytimes.com/2014/08/18/world/africa/new-larger-ebola-center-opens-in-liberia.html?&hp&action=click&pgtype=Homepage&version=LargeMediaHeadlineSum&module=photo-spot-region&region=photo-spot&WT.nav=photo-spot",
		content="Doctors Without Borders began accepting patients on Sunday at what is intended to be the largest-ever Ebola treatment center, near Monrovia, Liberias capital. The center is near two previous units, which have been filled beyond their intended capacity as the number of suspected Ebola patients in the capital grew greatly in recent days. The new unit, on the grounds of the Eternal Love Winning Africa mission hospital in Paynesville City, is designed to hold 120 patients and can be expanded to accommodate more than 300. There is an urgent need for it. On Sunday, patients who might be coming down with Ebola waited outdoors on the hospital grounds as a storm battered the city with rain. Nine patients were admitted to the new unit.",
		views=10)
	
	add_page(cat=Ebola_cat,
		title="3 Liberian Health Workers With Ebola Receive Scarce Drug After Appeals to U.S.",
		url="http://www.nytimes.com/2014/08/17/world/africa/three-liberian-health-workers-get-experimental-ebola-drug.html?action=click&contentCollection=Africa&region=Footer&module=MoreInSection&pgtype=article",
		content="Three Liberian health care workers who have contracted Ebola received an extremely scarce experimental serum on Friday at a hospital outside the national capital, Monrovia, a Liberian health official said Saturday. The official, Tolbert G. Nyenswah, an assistant minister of health and social welfare, would not say if any of the three were doctors. The drug, a mix of monoclonal antibodies called ZMapp, has been tested in animals, but has not been studied for safety or effectiveness in humans. It arrived in Liberia on Wednesday after appeals by leaders there to top officials in the United States and a letter from President Ellen Johnson Sirleaf of Liberia to President Obama.",
		views=20)
	
	add_page(cat=Ebola_cat,
		title="Hospitals in the U.S. Get Ready for Ebola",
		url="http://www.nytimes.com/2014/08/16/health/hospitals-in-the-us-get-ready-for-ebola.html?action=click&contentCollection=Africa&module=RelatedCoverage&region=Marginalia&pgtype=article",
		content="Hospitals nationwide are hustling to prepare for the first traveler from West Africa who arrives in the emergency room with symptoms of infection with the Ebola virus. Dr. Thomas R. Frieden, director of the Centers for Disease Control and Prevention, has said such a case is inevitable in the United States, and the agency this month issued the first extensive guidelines for hospitals on how recognize and treat Ebola patients. The recommendations touch on everything from the safe handling of lab specimens to effective isolation of suspected Ebola patients. But one piece of advice in particular has roused opposition from worried hospital administrators.",
		views=20)
	
	IsPal_cat = add_cat("Israel Palestine Conflict", 64, 32)
	
	add_page(cat=IsPal_cat,
		title="Artists Work Rises From the Destruction of the Israel-Gaza Conflict",
		url="http://www.nytimes.com/2014/08/17/world/middleeast/artists-work-rises-from-the-destruction-of-the-israel-gaza-conflict.html?ref=world",
		content="Khan Younis, Gaza Strip  The images of so many houses destroyed, so many bomb blasts, even so many bodies wrapped in burial shrouds can begin to blur together, indistinguishable. But Belal Khaled, a young photojournalist and painter in this southern Gaza town, saw symbols and stories in the smoke all around him. First, in a black cloud staining the bright blue sky above a beach, he saw hints of a prominent nose, thick mustache and wild hair, like an old man contemplating the situation of Gaza, Mr. Khaled said. Then, in a friends photograph of a taller, thinner plume, he saw a fist with the index finger extended, a gesture Muslims make when saying, No God but Allah. Using Photoshop, Mr. Khaled added a few simple lines to emphasize these hidden icons, and uploaded the artwork to Facebook, where it was shared and liked thousands of times.",
		views=15)
		
	add_page(cat=IsPal_cat,
		title="Agreeing to More Talks in Egypt, Israelis and Palestinians Begin Latest Cease-Fire",
		url= "http://www.nytimes.com/2014/08/11/world/middleeast/israel-gaza-strip-conflict.html?action=click&contentCollection=Middle%20East&module=RelatedCoverage&region=Marginalia&pgtype=article",
		content="Jerusalem  Israeli and Palestinian negotiators on Sunday accepted Egypts proposal for a new 72-hour cease-fire in the Gaza fighting, which began one minute after midnight on Monday, and agreed to resume Egyptian-mediated negotiations toward a more durable solution. But several previous cease-fires have collapsed or expired, followed by renewed fighting, and it was not immediately clear whether the sides had moved nearer to an agreement on the contested issues. The Palestinian negotiators have remained in Cairo since the last cease-fire expired on Friday. As that truce ended, Hamas, the Islamic group that dominates Gaza, fired barrages of rockets into Israel, prompting Israel to resume its airstrikes.",
		views=50)
		
	add_page(cat=IsPal_cat,
		title="Israelis and Gazans Clash, but Fighting Is More Subdued",
		url="http://www.nytimes.com/2014/08/10/world/middleeast/israel-gaza-strip-conflict-continues.html?action=click&contentCollection=Middle%20East&module=RelatedCoverage&region=Marginalia&pgtype=article",
		content="Cross-border hostilities between Gaza and Israel continued on Saturday, a day after a temporary cease-fire expired. But the simmering exchanges were on a lower scale than the fighting that has raged for most of the last month, as Egyptian-brokered efforts continued for a new cease-fire and a resumption of talks on a more durable end to the conflict. Eight Palestinians were reported killed in Israeli airstrikes, and Palestinian militants fired more rockets into Israel. No new Israeli casualties were reported. Hamas, the Islamist group that controls Gaza and is leading the Palestinian fighting, had refused to extend the 72-hour cease-fire that expired at 8 a.m. Friday and immediately fired salvos of rockets into Israel. The group was frustrated with what Palestinian officials said was a failure by Egypt and Israel to address Hamass demands for a full lifting of the blockade on Gaza and the construction of a seaport.",
		views=42)
	
	EasternUK_cat = add_cat("Rebels in Eastern Ukraine", 32, 16)
	
	add_page(cat=EasternUK_cat,
		title="Ukraine Says Rebels Shot Down Fighter Jet",
		url="http://bottlepy.org/docs/dev/",
		content="Kyiv, Ukraine  Army troops have penetrated deep inside a rebel-controlled city in eastern Ukraine in what could prove a breakthrough development in the four-month-long conflict, the Ukrainian government said Sunday. However, the military acknowledged that another one of its fighter planes was shot down by the separatists, who have been bullish about their ability to continue the battle and have bragged about receiving support from Russia. An Associated Press reporter spotted a column of several dozen heavy vehicles, including tanks and at least one rocket launcher, rolling through rebel-held territory on Sunday. Ukraine's national security council said government forces captured a district police station in Luhansk on Saturday after bitter clashes in the Velika Vergunka neighborhood.",
		views=3)
		
	add_page(cat=EasternUK_cat,
		title="In Another Rebel Setback, Ukraine Says Army Controls Center of Luhansk",
		url="http://www.nytimes.com/2014/08/18/world/europe/ukraine.html?action=click&contentCollection=Europe&region=Footer&module=MoreInSection&pgtype=article",
		content="Donetsk, Ukraine  The Ukrainian military on Sunday moved into the heart of the separatist hub of Luhansk for the first time, officials said, chipping at one of the cornerstones of the pro-Russian rebels disintegrating virtual state. Ukrainian officials said army units had raised the national flag over a police station in central Luhansk, the eastern city that, along with Donetsk, has been a center of rebel activity and an important destination for Russian fighters and aid. Other parts of Luhansk, however, were still said to be under rebel control. The claim could not be independently confirmed, though a photograph of the flag and police station was circulating on social media, and the report was consistent with the progress of fighting there going into the weekend.",
		views=5)
	
	for c in Category.objects.all():
		for p in Page.objects.filter(category=c):
			print "- {0} - {1}".format(str(c), str(p))
	
def add_page(cat, title, url, content, views=0):
	p = Page.objects.get_or_create(category=cat, title=title, url=url, content=content, views=views)[0]
	return p

def add_cat(name, views, likes):
	c = Category.objects.get_or_create(name=name, views=views, likes=likes)[0]
	return c

#start execution here!
if __name__ == '__main__':
	print "Starting Rango population script..."
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')
	from rango.models import Category, Page
	populate()