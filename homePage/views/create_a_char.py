from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login
from homePage import models as m
from . import templater
import glob

def process_request(request):
  from django import forms
  from django.conf import settings
  from django.http import HttpResponse, HttpResponseRedirect, Http404
  from django.contrib.auth import authenticate, login
  from homePage import models as m
  from . import templater
  import glob

def process_request(request):
  sign = m.Sign.objects.get(name = '589')
  line = 1
  new_char = m.AssyrianChar()
  new_char.id = 1
  new_char.line = line
  new_char.Sign = sign
  new_char.note = "6a74eaae-3c30-4661-a7fb-2adfc974df0b"
  new_char.save()

  sign = m.Sign.objects.get(name = '78')
  line = 1
  new_char = m.AssyrianChar()
  new_char.id = 2
  new_char.line = line
  new_char.Sign = sign
  new_char.note = "6fc68815-1ead-420c-8eb9-844a23491b75"
  new_char.save()

  sign = m.Sign.objects.get(name = '579')
  line = 1
  new_char = m.AssyrianChar()
  new_char.id = 3
  new_char.line = line
  new_char.Sign = sign
  new_char.note = "9f25034b-e28a-4459-ae5d-255372ed3098"
  new_char.save()

  sign = m.Sign.objects.get(name = '170')
  line = 1
  new_char = m.AssyrianChar()
  new_char.id = 4
  new_char.line = line
  new_char.Sign = sign
  new_char.note = "7fa1866d-993e-45f0-88f8-2aa8559ff7c0"
  new_char.save()

  sign = m.Sign.objects.get(name = '557')
  line = 1
  new_char = m.AssyrianChar()
  new_char.id = 5
  new_char.line = line
  new_char.Sign = sign
  new_char.note = "3336488b-f628-404c-b742-b6dee11fc348"
  new_char.save()

  sign = m.Sign.objects.get(name = '319')
  line = 2
  new_char = m.AssyrianChar()
  new_char.id = 6
  new_char.line = line
  new_char.Sign = sign
  new_char.note = "7fa1f185-7831-42ff-9bd0-9faa485626f3"
  new_char.save()

  sign = m.Sign.objects.get(name = '396a')
  line = 2
  new_char = m.AssyrianChar()
  new_char.id = 7
  new_char.line = line
  new_char.Sign = sign
  new_char.note = "1848f5e6-c0cd-4c6c-a05e-39527afe8a79"
  new_char.save()

  sign = m.Sign.objects.get(name = '335')
  line = 2
  new_char = m.AssyrianChar()
  new_char.id = 8
  new_char.line = line
  new_char.Sign = sign
  new_char.note = "f3e64cbc-5bdf-4354-bffc-8a979d90aef7"
  new_char.save()

  sign = m.Sign.objects.get(name = '579')
  line = 2
  new_char = m.AssyrianChar()
  new_char.id = 9
  new_char.line = line
  new_char.Sign = sign
  new_char.note = "d7512498-1f54-451b-86d6-5fa6ef3df3ee"
  new_char.save()

  sign = m.Sign.objects.get(name = '112')
  line = 2
  new_char = m.AssyrianChar()
  new_char.id = 10
  new_char.line = line
  new_char.Sign = sign
  new_char.note = "60a955c2-d106-4fda-866e-73499205842f"
  new_char.save()

  sign = m.Sign.objects.get(name = '532')
  line = 2
  new_char = m.AssyrianChar()
  new_char.id = 11
  new_char.line = line
  new_char.Sign = sign
  new_char.note = "8e10dd18-31d4-495b-b75b-91d2e5ef24a0"
  new_char.save()

  sign = m.Sign.objects.get(name = '399')
  line = 2
  new_char = m.AssyrianChar()
  new_char.id = 12
  new_char.line = line
  new_char.Sign = sign
  new_char.note = "1b59f811-a99a-46f3-bbdb-c48058ccaf52"
  new_char.save()

  sign = m.Sign.objects.get(name = '142')
  line = 3
  new_char = m.AssyrianChar()
  new_char.id = 13
  new_char.line = line
  new_char.Sign = sign
  new_char.note = "f928d175-18be-42e5-9b4d-8b4bfeae4545"
  new_char.save()

  sign = m.Sign.objects.get(name = '396a')
  line = 3
  new_char = m.AssyrianChar()
  new_char.id = 14
  new_char.line = line
  new_char.Sign = sign
  new_char.note = "5ed612b4-a20d-4aac-a1fb-874409fe21d8"
  new_char.save()

  sign = m.Sign.objects.get(name = '148')
  line = 3
  new_char = m.AssyrianChar()
  new_char.id = 15
  new_char.line = line
  new_char.Sign = sign
  new_char.note = "87e1d11e-906a-4389-8ce6-5e6c4e84fb6f"
  new_char.save()

  sign = m.Sign.objects.get(name = '342')
  line = 3
  new_char = m.AssyrianChar()
  new_char.id = 16
  new_char.line = line
  new_char.Sign = sign
  new_char.note = "658700b4-1170-437b-b035-599121ff4764"
  new_char.save()

  sign = m.Sign.objects.get(name = '579')
  line = 4
  new_char = m.AssyrianChar()
  new_char.id = 17
  new_char.line = line
  new_char.Sign = sign
  new_char.note = "49736074-a7d8-422e-9824-87be6c0ee80a"
  new_char.save()

  sign = m.Sign.objects.get(name = '70')
  line = 4
  new_char = m.AssyrianChar()
  new_char.id = 18
  new_char.line = line
  new_char.Sign = sign
  new_char.note = "5df86a86-bf07-4a7b-8440-594fe1c1df42"
  new_char.save()

  sign = m.Sign.objects.get(name = '598a')
  line = 4
  new_char = m.AssyrianChar()
  new_char.id = 19
  new_char.line = line
  new_char.Sign = sign
  new_char.note = "d3cf7ecd-38d7-415f-b293-75a06faadbba"
  new_char.save()

  sign = m.Sign.objects.get(name = '595')
  line = 4
  new_char = m.AssyrianChar()
  new_char.id = 20
  new_char.line = line
  new_char.Sign = sign
  new_char.note = "f053847d-ce61-4a2f-8caf-dfe97d4d9d4d"
  new_char.save()

  sign = m.Sign.objects.get(name = '468')
  line = 4
  new_char = m.AssyrianChar()
  new_char.id = 21
  new_char.line = line
  new_char.Sign = sign
  new_char.note = "49b69885-7666-49b8-9f88-9efd70a8cafd"
  new_char.save()

  sign = m.Sign.objects.get(name = '381')
  line = 4
  new_char = m.AssyrianChar()
  new_char.id = 22
  new_char.line = line
  new_char.Sign = sign
  new_char.note = "1789d20d-9d90-4fcd-83a5-d1a9ba987c37"
  new_char.save()

  sign = m.Sign.objects.get(name = '319')
  line = 5
  new_char = m.AssyrianChar()
  new_char.id = 23
  new_char.line = line
  new_char.Sign = sign
  new_char.note = "4ff057e6-9f0a-4d19-aa93-a4fa57e74826"
  new_char.save()

  sign = m.Sign.objects.get(name = '319')
  line = 5
  new_char = m.AssyrianChar()
  new_char.id = 24
  new_char.line = line
  new_char.Sign = sign
  new_char.note = "47c688b5-408b-4cbd-87f0-ce894aad3121"
  new_char.save()

  sign = m.Sign.objects.get(name = '86')
  line = 5
  new_char = m.AssyrianChar()
  new_char.id = 25
  new_char.line = line
  new_char.Sign = sign
  new_char.note = "ebbac1d6-121e-4c70-bb3a-b8e358d5fec9"
  new_char.save()

  sign = m.Sign.objects.get(name = '579')
  line = 5
  new_char = m.AssyrianChar()
  new_char.id = 26
  new_char.line = line
  new_char.Sign = sign
  new_char.note = "5daf6862-f961-4f4e-a2ff-625ea3b74f8b"
  new_char.save()

  sign = m.Sign.objects.get(name = '212')
  line = 6
  new_char = m.AssyrianChar()
  new_char.id = 27
  new_char.line = line
  new_char.Sign = sign
  new_char.note = "865f4680-019c-4356-81d5-fd82131b70e3"
  new_char.save()

  sign = m.Sign.objects.get(name = '579')
  line = 6
  new_char = m.AssyrianChar()
  new_char.id = 28
  new_char.line = line
  new_char.Sign = sign
  new_char.note = "943fdd75-ead6-485e-b089-0dcf0d93d9de"
  new_char.save()

  sign = m.Sign.objects.get(name = '170')
  line = 6
  new_char = m.AssyrianChar()
  new_char.id = 29
  new_char.line = line
  new_char.Sign = sign
  new_char.note = "0b3efae9-f633-4354-906f-f860c96326c8"
  new_char.save()

  sign = m.Sign.objects.get(name = '112')
  line = 6
  new_char = m.AssyrianChar()
  new_char.id = 30
  new_char.line = line
  new_char.Sign = sign
  new_char.note = "ebfc3dbf-aed6-4b62-89cf-3450235c78e4"
  new_char.save()

  sign = m.Sign.objects.get(name = '354a')
  line = 6
  new_char = m.AssyrianChar()
  new_char.id = 31
  new_char.line = line
  new_char.Sign = sign
  new_char.note = "1d6f0582-fccc-4657-87bb-7ebfb713228d"
  new_char.save()

  sign = m.Sign.objects.get(name = '342')
  line = 6
  new_char = m.AssyrianChar()
  new_char.id = 32
  new_char.line = line
  new_char.Sign = sign
  new_char.note = "f7da5f84-74e0-4ae8-9fb5-661698bea15d"
  new_char.save()

  sign = m.Sign.objects.get(name = '342')
  line = 7
  new_char = m.AssyrianChar()
  new_char.id = 33
  new_char.line = line
  new_char.Sign = sign
  new_char.note = "55970697-e8e9-4ec7-b84a-cfc521ff1fed"
  new_char.save()

  sign = m.Sign.objects.get(name = '342')
  line = 7
  new_char = m.AssyrianChar()
  new_char.id = 34
  new_char.line = line
  new_char.Sign = sign
  new_char.note = "7ca1c742-48f7-4dcc-ae2b-e69ecc122373"
  new_char.save()

  sign = m.Sign.objects.get(name = '13')
  line = 7
  new_char = m.AssyrianChar()
  new_char.id = 35
  new_char.line = line
  new_char.Sign = sign
  new_char.note = "1addafae-e4f9-44e2-9f53-966f92abdfff"
  new_char.save()

  sign = m.Sign.objects.get(name = '579')
  line = 7
  new_char = m.AssyrianChar()
  new_char.id = 36
  new_char.line = line
  new_char.Sign = sign
  new_char.note = "3dc4805f-c487-47a8-9c56-67302a21912b"
  new_char.save()

  sign = m.Sign.objects.get(name = '70')
  line = 8
  new_char = m.AssyrianChar()
  new_char.id = 37
  new_char.line = line
  new_char.Sign = sign
  new_char.note = "bb0269e6-f295-4267-b060-70e888354219"
  new_char.save()

  sign = m.Sign.objects.get(name = '319')
  line = 8
  new_char = m.AssyrianChar()
  new_char.id = 38
  new_char.line = line
  new_char.Sign = sign
  new_char.note = "3c2e55ea-24f4-45f8-bc72-ba48b79dcfd0"
  new_char.save()

  sign = m.Sign.objects.get(name = '319')
  line = 8
  new_char = m.AssyrianChar()
  new_char.id = 39
  new_char.line = line
  new_char.Sign = sign
  new_char.note = "ca4176e1-fb25-4815-99e2-527e1dd9bc04"
  new_char.save()

  sign = m.Sign.objects.get(name = '86')
  line = 8
  new_char = m.AssyrianChar()
  new_char.id = 40
  new_char.line = line
  new_char.Sign = sign
  new_char.note = "4799ca5d-791b-4cd6-b009-99b64ff6f3e3"
  new_char.save()

  sign = m.Sign.objects.get(name = '579')
  line = 9
  new_char = m.AssyrianChar()
  new_char.id = 41
  new_char.line = line
  new_char.Sign = sign
  new_char.note = "8a312545-2bd5-48e3-8187-0f1c5b0393ba"
  new_char.save()

  sign = m.Sign.objects.get(name = '142')
  line = 9
  new_char = m.AssyrianChar()
  new_char.id = 42
  new_char.line = line
  new_char.Sign = sign
  new_char.note = "214ae14d-fd18-4197-b76c-afc303d2cb39"
  new_char.save()

  sign = m.Sign.objects.get(name = '206')
  line = 9
  new_char = m.AssyrianChar()
  new_char.id = 43
  new_char.line = line
  new_char.Sign = sign
  new_char.note = "43be12c1-7216-421c-8161-2b13cf348835"
  new_char.save()

  sign = m.Sign.objects.get(name = '383')
  line = 9
  new_char = m.AssyrianChar()
  new_char.id = 44
  new_char.line = line
  new_char.Sign = sign
  new_char.note = "5073b62d-d285-41c7-a573-c83ad993ca27"
  new_char.save()

  # sign = m.Sign.objects.get(name = '451')
  # line = 9
  # new_char = m.AssyrianChar()
  # new_char.id = 45
  # new_char.line = line
  # new_char.Sign = sign
  # new_char.note = "14235979-31be-4dea-9778-80584272915e"
  # new_char.save()

  tvars = {
  }
  return templater.render_to_response(request, 'index.html', tvars)
