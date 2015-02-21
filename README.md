#Talatat

An exploratory API for the ConcertTalent.com website, which is presently being refactored as one of two potential frontend clients: Stradivarius (a Django client) or Guarnerius (an Angular client). This API is for experimenting with API calls only and not intended for production use.


###ABOUT TALATAT

Name for small blocks of sandstone used to construct Akhenaten's Aten temples and palaces in ancient Egypt. Due to their handy and uniform size, they expedited building things and structures that used them were often later dismantled and the blocks were reused in other constructions. The origin of the term talatat is supposedly originates with the Arabic word for "three", insomuch as the dimension of a talatat was three palm-widths.


###TECHNOLOGY STACK

Talatat is built on Pyramid (a Python framework)--and is easily installed on an AWS EC2 server (Linux Ubuntu 14.04 LTS) associated with an Elastic IP, or any cloud service provider you choose. The Concert Talent API will likely be refactored as an Eve app or as a Sandman app. But, if you're looking for an example of a lightweight API running on a relatively fast and agnostic Python framework, this might be a good place to start. (Special thanks to Jakub Nowak--who's work upon which this API is based.)

###INSTALLATION AND USE

You'll need to set up a virtual environment on your local machine, as per 
any proper Python project. Virtualenvwrapper is also recommended.

Right now, assuming you already have Mongo installed, and assuming you've
cloned the repo onto your local machine and have run setup.py as per
Pyramid's offical docs, you can then load up the included fixture of JSON data into your local Mongo instance via running the following at the command line...

    mongoimport --db musicians --collection musicians --type json --file fixture.json --jsonArray

Then start up the app locally via...

    pserve --reload development.ini
    
As an example, you can GET a list of all musician data in JSON format via...

    http://localhost:8080/musicians
    
...or a specific musician's data via...

    http://localhost:8080/musicians/<mongo_id>



###SETTINGS

Talatat's settings may be managed via environment variables and the development or production .ini files as suggested by the official Pyramid documentation.
 
------------------------------------------------------------------------

###LICENSE AND CONTACT INFO

Copyright © 2015 by BlogBlimp.

All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDER AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

If you're a developer interested in checking out the site, or interested in using a fork of any part of Concert Talent's components for commercial purposes, please kindly give me a heads-up at:

sean@blogblimp.com
