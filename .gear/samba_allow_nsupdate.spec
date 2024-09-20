%define script_name samba_allow_nsupdate

Name: samba_allow_nsupdate
Version: 0.1
Release: alt1

Summary: Utility for managing the rights of domain computers to their DNS records
License: GPLv3
URL: https://github.com/altlinuxteam/samba_allow_nsupdate
VCS: https://github.com/altlinuxteam/samba_allow_nsupdate

BuildArch: noarch
Group: System/Configuration/Networking
Source: %name-%version.tar

BuildRequires: shellcheck


%description
The %{name} utility allows setting permissions for domain computers 
on their DNS records. You can select either individual computers
by their names or SIDs or allow all computers in the domain to update
their DNS records.

%prep
%setup

%install
install -Dm 755 %script_name %buildroot/%_bindir/%script_name
install -Dm 644 doc/samba_allow_nsupdate.1 %buildroot/%_man1dir/samba_allow_nsupdate.1

%check
shellcheck %script_name

%files
%_bindir/%script_name
%_man1dir/samba_allow_nsupdate.1.*

%changelog
* Thu Sep 12 2024 Your Name <kamaevaoi@altlinux.org> 0.1-alt1
- Initial release.