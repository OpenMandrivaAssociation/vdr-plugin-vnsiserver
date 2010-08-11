
%define plugin	vnsiserver
%define name	vdr-plugin-%plugin
%define version	0.0.1
%define snap	32590
%define rel	1

Summary:	VDR plugin: VDR-Network-Streaming-Interface (VNSI) Server
Name:		%name
Version:	%version
Release:	%mkrel 0.svn%snap.%rel
Group:		Video
License:	GPLv2+
URL:		http://xbmc.org/

# URL=https://xbmc.svn.sourceforge.net/svnroot/xbmc/branches/pvr-testing2/xbmc/pvrclients/vdr-vnsi/vdr-plugin-vnsiserver
# REV=$(svn info $URL| sed -ne 's/^Last Changed Rev: //p')
# svn export -r $REV $URL vnsiserver-$REV
# tar -cjf vdr-vnsiserver-$REV.tar.bz2 vnsiserver-$REV
Source:		vdr-%plugin-%snap.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
A VNSI server for VDR, allowing the use of VDR via VNSI PVR addon of XBMC.

%prep
%setup -q -n %plugin-%snap
%apply_patches
%vdr_plugin_prep

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

install -m755 -d %{buildroot}%{_vdr_plugin_cfgdir}/%{plugin}
install -m644 %{plugin}/* %{buildroot}%{_vdr_plugin_cfgdir}/%{plugin}

install -m755 -d %{buildroot}%{_vdr_plugin_datadir}/%{plugin}
mv %{buildroot}%{_vdr_plugin_cfgdir}/%{plugin}/noSignal.mpg %{buildroot}%{_vdr_plugin_datadir}/%{plugin}
ln -s %{_vdr_plugin_datadir}/%{plugin}/noSignal.mpg %{buildroot}%{_vdr_plugin_cfgdir}/%{plugin}/noSignal.mpg

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY
%dir %{_vdr_plugin_cfgdir}/%{plugin}
%config(noreplace) %{_vdr_plugin_cfgdir}/%{plugin}/allowed_hosts.conf
%config(noreplace) %{_vdr_plugin_cfgdir}/%{plugin}/noSignal.mpg
%dir %{_vdr_plugin_datadir}/%{plugin}
%{_vdr_plugin_datadir}/%{plugin}/noSignal.mpg

