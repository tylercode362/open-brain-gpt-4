INTRO
=====

This is a proof of concept for the future of programming.

Ideally, `main.py` should not require frequent updates.
Instead, all modifications can be made in `spec.md`.

If `spec.md` is thoughtfully designed, it can enable AI to
understand your intentions. Then, all that's necessary is
to collect the response and forward it to other endpoints.

The current output looks like this:

```
http://10.1.1.12:3000/apis/fence?action=down
http://10.1.1.11:3000/apis/sound?level=10&duration=5
http://10.1.1.13:3000/apis/report?description=There is a car on the railway crossing. Please take immediate action.
```

This means that, based on the current camera image,
the AI has determined that it should activate the alarm,
lower the fence, and alert the control center.
