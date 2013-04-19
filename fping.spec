Summary:	Quickly ping N number of hosts to determine their reachability
Name:		fping
Version:	3.4
Release:	1
License:	BSD
Group:		Networking/Other
Url:		http://fping.org/
Source0:	http://fping.org/dist/fping-%{version}.tar.gz

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
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files 
%doc README INSTALL ChangeLog
%attr(4755,root,root) %{_sbindir}/fping
%{_mandir}/man8/fping.8*

