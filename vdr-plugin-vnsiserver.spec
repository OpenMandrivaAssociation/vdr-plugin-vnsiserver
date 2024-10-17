
%define plugin	vnsiserver
%define name	vdr-plugin-%plugin
%define version	0.0.1
%define snap	32590
%define rel	3

Summary:	VDR plugin: VDR-Network-Streaming-Interface (VNSI) Server
Name:		%name
Version:	%version
Release:	0.svn%snap.%rel
Group:		Video
License:	GPLv2+
URL:		https://xbmc.org/

# URL=https://xbmc.svn.sourceforge.net/svnroot/xbmc/branches/pvr-testing2/xbmc/pvrclients/vdr-vnsi/vdr-plugin-vnsiserver
# REV=$(svn info $URL| sed -ne 's/^Last Changed Rev: //p')
# svn export -r $REV $URL vnsiserver-$REV
# tar -cjf vdr-vnsiserver-$REV.tar.bz2 vnsiserver-$REV
Source:		vdr-%plugin-%snap.tar.bz2
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
A VNSI server for VDR, allowing the use of VDR via VNSI PVR addon of XBMC.

%prep
%setup -q -n %plugin-%snap
%autopatch -p1
%vdr_plugin_prep

%build
%vdr_plugin_build

%install
%vdr_plugin_install

install -m755 -d %{buildroot}%{vdr_plugin_cfgdir}/%{plugin}
install -m644 %{plugin}/* %{buildroot}%{vdr_plugin_cfgdir}/%{plugin}

install -m755 -d %{buildroot}%{vdr_plugin_datadir}/%{plugin}
mv %{buildroot}%{vdr_plugin_cfgdir}/%{plugin}/noSignal.mpg %{buildroot}%{vdr_plugin_datadir}/%{plugin}
ln -s %{vdr_plugin_datadir}/%{plugin}/noSignal.mpg %{buildroot}%{vdr_plugin_cfgdir}/%{plugin}/noSignal.mpg

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY
%dir %{vdr_plugin_cfgdir}/%{plugin}
%config(noreplace) %{vdr_plugin_cfgdir}/%{plugin}/allowed_hosts.conf
%config(noreplace) %{vdr_plugin_cfgdir}/%{plugin}/noSignal.mpg
%dir %{vdr_plugin_datadir}/%{plugin}
%{vdr_plugin_datadir}/%{plugin}/noSignal.mpg



%changelog
* Wed Aug 11 2010 Anssi Hannula <anssi@mandriva.org> 0.0.1-0.svn32590.1mdv2011.0
+ Revision: 569119
- new snapshot (fixes issues with config files)
- config files moved to proper location and marked as noreplace
- drop upstreamed patch

* Sat Aug 07 2010 Anssi Hannula <anssi@mandriva.org> 0.0.1-0.svn32585.2mdv2011.0
+ Revision: 567441
- fix crash when a recording has no title in path and no event info

* Sat Aug 07 2010 Anssi Hannula <anssi@mandriva.org> 0.0.1-0.svn32585.1mdv2011.0
+ Revision: 567417
- initial Mandriva release

