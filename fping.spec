Summary:	Quickly ping N number of hosts to determine their reachability
Name:		fping
Version:	2.4b2
Release:	%mkrel 11
License:	GPL
Group:		Networking/Other
URL:		http://www.fping.com/
Source0:	fping-2.4b2_to-ipv6.tar.bz2
Patch0:		fping-2.4b2_to-ipv6-debian_fix.diff
BuildRequires:	autoconf2.5
BuildRequires:	automake1.7
BuildRequires:	libtool
BuildRoot:	%{_tmppath}/%{name}-root

%description
fping is a ping(1) like program which uses the Internet Control Message
Protocol (ICMP) echo request to determine if a host is up. fping is different
from ping in that you can specify any  number of hosts on the command line, or
specify a file containing the lists of hosts to ping. Instead of trying one
host until it timeouts or replies, fping will send out a ping packet and move
on to the next host in a round-robin fashion. If a host replies, it is noted
and removed from the list of hosts to check. If a host does not respond within
a certain time limit and/or retry limit it will be considered unreachable.

%prep

%setup -q -n fping-2.4b2_to-ipv6
%patch0 -p0

# fix strange perms
chmod 644 README INSTALL ChangeLog

%build
export WANT_AUTOCONF_2_5="1"
rm -f configure; libtoolize --copy --force; aclocal-1.7; automake-1.7 --add-missing; autoconf

%configure2_5x \
    --bindir=/bin \
    --sbindir=/bin

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README INSTALL ChangeLog
%attr(4755,root,root) /bin/fping
%{_mandir}/man8/fping.8*


