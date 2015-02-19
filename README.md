#Talatat
####an exploratory API for the ConcertTalent.com website, which is being refactored as one of two potential frontend clients: Stradivarius (a Django client) or Guarnerius (an Angular client).

###ABOUT TALATAT
Name for small blocks of sandstone used to construct Akhenaten's Aten temples and palaces in ancient Egypt. Due to their handy and uniform size, they expedited building things and structures that used them were often later dismantled and the blocks were reused in other constructions. The origin of the term talatat is supposedly originates with the Arabic word for "three", insomuch as the dimension of a talatat was three palm-widths.

###TECHNOLOGY STACK
Talatat is built on Pyramid (a Python framework)--and ultimately installed on an AWS EC2 server (Linux Ubuntu 14.04 LTS) associated with an Elastic IP. (The Concert Talent API may ultimtely be refactored as an Eve app or as a Sandman app.)


Right now, you can clone the repo and run locally via...

    pserve --reload development.ini
    
You can access musician data via...

    http://localhost:8080/musicians
    
...or...

    http://localhost:8080/musicians/<name>

###SETTINGS
Talatat's settings can be managed via environment variables and the development or production .ini files as suggested by the [official documentation] (http://docs.pylonsproject.org/projects/pyramid/en/latest/narr/environment.html#environment-chapter).  
------------------------------------------------------------------------

###LICENSE AND CONTACT INFO

Copyright © 2015 by Sean Bradley.

All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDER AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

If you're a developer interested in checking out the site, or interested in using a fork of Stradivarius for commercial purposes, please kindly give me a heads-up at:

sean@blogblimp.com
