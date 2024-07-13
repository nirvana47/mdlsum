# test_summarize.py
from summarize import summarize_text

text = """The President of the United States, Joe Biden.
 Thank you, please, I see it.
 President Biden in a closely watched press conference on Thursday
 calmed down some of the most nervous Democrats,
 but it remains to be seen if he's done enough to see of his candidacy.
 President Biden's performance of the press conference was pretty consistent with what
 people who watch the president closely would see.
 He had the same kind of strong moments and weak moments that he has had at
 sort of multiple press conferences over the last few months.
 What has changed is the scrutiny on him is much, much more intense.
 I'm not in this for my legacy.
 I'm in this to complete the job I started.
 The stakes for this were extremely high for the president.
 He has been, since the debate, on this sort of cleanup tour,
 trying to do a number of things to show that he has the mental
 acuity to continue to run the country.
 I beat him once and I will beat him again.
 He had some flubs early on.
 He mixed up Vice President Trump when he meant to say Vice President Harris.
 I wouldn't have picked Vice President Trump to be Vice President
 but I think she's not qualified to be president.
 The press conference showed him the way he is.
 You know, he's an 81-year-old man and, you know, he does have really good moments
 and he has a deep knowledge of foreign policy, which was very clearly on display.
 So there's a lot of things in retrospect.
 I wish I had been able to convince the Israelis to do.
 But the bottom line is we have a chance now.
 It's time to end this war.
 It doesn't mean walk away from going after Sinwar and Hamas.
 There are questions about whether or not he would be able to physically do this job
 in two or three years.
 Already, he has said, "I'm not as good of a debater than I used to be.
 I want to shift my schedule so that I'm doing fewer things later at night."
 Instead of my every day starting at seven and going to bed at midnight,
 it'd be smarter for me to pace myself a little more.
 He was a little reflective, I think, and I think that is something that there has been
 a desire for among Democrats that I've talked to at least.
 He was asked at the very end what it would take for him to leave the race.
 If your team came back and showed you data that she would fair better against former President
 Donald Trump, would you reconsider your decision to stay in the race?
 No, unless they came back and said, "There's no way you can win."
 Me. Don't say that.
 The Democratic Party going into this press conference is in complete disarray.
 There have been about a dozen lawmakers at this point, elected members of Congress
 who are Democrats who have called on President Biden to drop out of the presidential race.
 Talking to donors who were texting me during the press conference
 is that there's this fear that they have when they're watching him.
 That, "Oh my gosh, is it going to be okay?
 Are we going to see the debate version of Joe Biden again?
 Or is he going to get through it?"
 And there's this heightened anxiety every time he is talking.
 And so our military is where I'm following the advice of my commander and chief,
 my chief of staff at the military, as well as the secretary of defense, and our intelligence people.
 And that's also playing into the sense of, I don't know,
 four months is really a lifetime in politics.
 Can we really ride this horse all the way to November?
 There's a kind of anticipation and anxiety in the White House about
 whether there's going to be an onslaught of additional Democratic leaders
 who are going to call on the president to drop out.
 And if you think of it as a sort of a dam that's about to break, it is leaking.
 It is a leaky dam. It is sort of about to break.
 There is, you know, one theory by people who are close to Biden's advisors,
 which is that the president really has up to this weekend
 to make a final, final decision.
 And the thing that is going to change,
 and this is the mind of many of the Biden people and the people close to the Biden's,
 is that the Republican convention starts on Monday.
 And for them, they believe that the sort of glare of the media
 is going to shift away from Joe Biden and onto Donald Trump.
 And that is really where they want the attention to be.
 You"""
summary = summarize_text(text)
print(f"Summary: {summary}")