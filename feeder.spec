Summary:	Support for compressed usenet feeds
Summary(pl.UTF-8):	Obsługa feedu kompresowanych newsów
Name:		feeder
Version:	2.1.4
%define	oldver	0.99
Release:	10
License:	GPL
Group:		Applications/News
#Source0:	http://newsy.media-com.com.pl/scripts2/%{name}-%{version}.tar.gz
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	ef1789496a616c2ed443b540707e446c
#Source1:	http://newsy.media-com.com.pl/scripts2/server-script/fetcher
Source1:	fetcher
# taken and rpm2cpioed from http://www.media-com.com.pl/~radecki/scripts/feeder-0.99-pre6.src.rpm
Source2:	%{name}-%{oldver}.tar.gz
# Source2-md5:	202e4317dcd98b793dfcf12c0ffcc855
# taken from http://newsy.karnet.pl/, currently unused
#Source3:	%{name}-sd
#Source4:	%{name}-sd.conf
#URL:		http://newsy.media-com.com.pl/
Patch0:		%{name}-%{oldver}-url_n_notermcap.patch
Patch1:		%{name}-next.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A set of client scripts for downloading compressed newsfeed and
transfering it to a local (proxy)newsserver.

%description -l pl.UTF-8
Zestaw skryptów klienckich do ściągania i transferu do lokalnego
(proxy)newsserwera postów w kompresowanych paczkach.

%package server
Summary:	Support for compressed usenet feeds - server side
Summary(pl.UTF-8):	Obsługa feedu kompresowanych newsów - skrypt serwerowy
Group:		Applications/News

%description server
A set of server scripts for downloading compressed newsfeed and
transfering it to a local (proxy)newsserver.

%description server -l pl.UTF-8
Zestaw skryptów serwerowych do ściągania i transferu do lokalnego
(proxy)newsserwera postów w kompresowanych paczkach i udostępniania
ich klientom.

%package old
Summary:	Support for compressed usenet feeds - old unauthorizing client
Summary(pl.UTF-8):	Obsługa feedu kompresowanych newsów - stary nie autoryzujący się klient
Version:	%{oldver}
Epoch:		1
Group:		Applications/News

%description old
A set of client scripts for downloading compressed newsfeed and
transfering it to a local (proxy)newsserver, this one does not require
authorizing with server, but it only downloads articles, you need some
nttp utilities to post news. (rpost might be good start)
NOTE: binaries have been prefixed with sigle 'o' character for
distinguishing from new feeder.
NOTE2: the pld.* hierarchy from news.wsisiz.edu.pl is automagically
added to groups file.

%description old -l pl.UTF-8
Zestaw skryptów klienckich do ściągania i transferu do lokalnego
newsserwera; skrypty te nie wymagają autoryzacji z serwerem news, ale
nie umożliwiają wysyłania artykułów; konieczne są dodatkowe narzędzia,
aby wysyłać artykuły do zdalnych serwerów (rpost może być dobrym
początkiem).
UWAGA: przez nazwami skryptów wykonywalnych dodano literkę 'o' aby
rozróżnić nowy feeder od starego.
UWAGA2: hierarchia grup pld.* z news.wsisiz.edu.pl została
automagicznie dodana do pliku groups.

%package old-ppp
Summary:	Automagic get-news on ppp-up
Summary(pl.UTF-8):	Automagiczne pobieranie paczek po podniesieniu ppp
Version:	%{oldver}
Epoch:		1
Group:		Applications/News
Requires:	%{name}-old = 1:%{oldver}

%description old-ppp
This will automagically fetch news after ppp-up.

%description old-ppp -l pl.UTF-8
Ten pakiet automagicznie ściągnie paczki po ppp-up.

%prep
%setup -q -a2
%patch -P0 -p0
%patch -P1 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/sysconfig/interfaces/up.d/ppp \
	$RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{perl_vendorlib}/Feeder} \
	$RPM_BUILD_ROOT%{_mandir}/pl/man{1,5,7} \
	$RPM_BUILD_ROOT%{_var}/spool/{%{name}2,%{name}}/{archive,received,old,tmp}

install etc/feeder.conf $RPM_BUILD_ROOT%{_sysconfdir}
install usr/lib/perl5/site_perl/Feeder/feeder.pm $RPM_BUILD_ROOT%{perl_vendorlib}/Feeder
install usr/local/bin/* $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_sbindir}
install usr/local/share/man/pl/man1/* $RPM_BUILD_ROOT%{_mandir}/pl/man1
install usr/local/share/man/pl/man5/* $RPM_BUILD_ROOT%{_mandir}/pl/man5
install usr/local/share/man/pl/man7/* $RPM_BUILD_ROOT%{_mandir}/pl/man7
install var/spool/feeder2/* $RPM_BUILD_ROOT%{_var}/spool/%{name}2

install feeder-%{oldver}/usr/bin/feed2inn $RPM_BUILD_ROOT%{_bindir}/ofeed2inn
install feeder-%{oldver}/usr/bin/feed2slrnpull_a $RPM_BUILD_ROOT%{_bindir}/ofeed2slrnpull_a
install feeder-%{oldver}/usr/bin/feed2slrnpull_b $RPM_BUILD_ROOT%{_bindir}/ofeed2slrnpull_b
install feeder-%{oldver}/usr/bin/news.put $RPM_BUILD_ROOT%{_bindir}/onews.put
install feeder-%{oldver}/usr/bin/news.send $RPM_BUILD_ROOT%{_bindir}/onews.send
install feeder-%{oldver}/usr/bin/suckem_perl $RPM_BUILD_ROOT%{_bindir}/osuckem_perl
install feeder-%{oldver}/usr/bin/suckem_sh $RPM_BUILD_ROOT%{_bindir}/osuckem_sh

install %{name}-%{oldver}/var/spool/news/feeder/last $RPM_BUILD_ROOT%{_var}/spool/%{name}
install %{name}-%{oldver}/var/spool/news/feeder/grupy $RPM_BUILD_ROOT%{_var}/spool/%{name}/groups

cat << EOF >> $RPM_BUILD_ROOT%{_var}/spool/%{name}/groups
pld.betatesters -100
pld.cvs.commit -100
pld.devel.en -100
pld.devel.pl -100
pld.discuss.pl -100
pld.installer -100
pld.kernel -100
pld.rc.scripts -100
pld.users.en -100
pld.users.pl -100
pld.www -100
EOF

cat << EOF > $RPM_BUILD_ROOT/etc/sysconfig/interfaces/up.d/ppp/feeder
#!/bin/sh

( ( sleep 15; /usr/bin/osuckem_perl -q ; /usr/bin/ofeed2inn -a ) 2>&1 | mail \
-s "feeder ppp-on, started on $(date)" news ) &

EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/feed2*
%attr(755,root,root) %{_bindir}/get-news
%{perl_vendorlib}/Feeder
%attr(660,root,news) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.conf
%attr(755,news,news) %dir %{_var}/spool/%{name}2
%attr(2775,news,news) %dir %{_var}/spool/%{name}2/archive
%attr(2775,news,news) %dir %{_var}/spool/%{name}2/received
%attr(664,news,news) %config(noreplace) %verify(not md5 mtime size) %{_var}/spool/%{name}2/groups
%attr(664,news,news) %config(noreplace) %verify(not md5 mtime size) %{_var}/spool/%{name}2/killfile
%lang(pl) %{_mandir}/pl/man?/*

%files server
%defattr(644,root,root,755)
%attr(755,news,news) %{_sbindir}/*

%files old
%defattr(644,root,root,755)
%doc feeder-%{oldver}/TODO
%attr(755,root,root) %{_bindir}/ofeed2inn
%attr(755,root,root) %{_bindir}/ofeed2slrnpull_a
%attr(755,root,root) %{_bindir}/ofeed2slrnpull_b
%attr(755,root,root) %{_bindir}/onews.put
%attr(755,root,root) %{_bindir}/onews.send
%attr(755,root,root) %{_bindir}/osuckem_perl
%attr(755,root,root) %{_bindir}/osuckem_sh
%attr(755,news,news) %dir %{_var}/spool/%{name}
%attr(2775,news,news) %dir %{_var}/spool/%{name}/old
%attr(2775,news,news) %dir %{_var}/spool/%{name}/received
%attr(2775,news,news) %dir %{_var}/spool/%{name}/tmp
%attr(664,news,news) %config(noreplace) %verify(not md5 mtime size) %{_var}/spool/%{name}/groups
%attr(664,news,news) %config(noreplace) %verify(not md5 mtime size) %{_var}/spool/%{name}/last

%files old-ppp
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/interfaces/up.d/ppp/feeder
