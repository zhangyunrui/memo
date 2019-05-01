from mailchimp3 import MailChimp
from mailchimp3.mailchimpclient import MailChimpError

mail_chimp_key = 'd0141d2ace4b9650159c9ce5d0587310-us12'
mail_chimp_name = 'Alex'
mail_chimp_list_id = 'ef24356674'
mail_chimp_template_id = 291745
mail_chimp_saved_segment_id = 185789
email = '635798274@qq.com'
name = 'zhangyunrui'

mc_client = MailChimp(
    mc_api=mail_chimp_key,
    mc_user=mail_chimp_name)

try:
    # create member
    mc_client.lists.members.create(
        list_id=mail_chimp_list_id,  # choose list
        data={
            "email_address": email,
            "status": "subscribed",
            "last_name": name})
except MailChimpError as e:
    print(str(e))
else:
    # create campaigns
    campaign = mc_client.campaigns.create(
        data={
            "recipients": {
                "list_id": mail_chimp_list_id,  # choose list
                "segment_opts": {
                    # choose segment(add_time after lasted sent campaign)
                    "saved_segment_id": int(mail_chimp_saved_segment_id)}},
            "type": "regular",
            "settings": {
                # choose template
                # (Flexible call) *|IF:FNAME|*Hi *|TITLE:FNAME|*,*|ELSE:|*Hello,*|END:IF|*
                "template_id": int(mail_chimp_template_id),  # choose template
                "subject_line": "Mercku Welcome",
                "reply_to": "Alex@Mercku.tech",
                "from_name": "Mercku"}})
    if isinstance(campaign, dict) and campaign.get("id", ""):
        mc_client.campaigns.actions.send(campaign_id=campaign["id"])
    else:
        print("create_campaigns wrong")
