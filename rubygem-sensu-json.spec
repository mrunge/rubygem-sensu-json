# Generated from sensu-json-1.1.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name sensu-json

Name:           rubygem-%{gem_name}
Version:        2.0.1
Release:        1%{?dist}
Summary:        The Sensu JSON parser abstraction library
Group:          Development/Languages
License:        MIT
URL:            https://github.com/sensu/sensu-json
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
BuildRequires:  ruby
%if 0%{?fedora} > 21
BuildRequires:  rubygem(rspec2)
%else
BuildRequires:  rubygem(rspec)
%endif
BuildRequires:  rubygem(oj)

Requires:       rubygem(oj)

BuildArch:      noarch

%if 0%{?rhel} > 0
Provides: rubygem(%{gem_name}) = %{version}
%endif

%description
The Sensu JSON parser abstraction library.

%package doc
Summary:        Documentation for %{name}
Group:          Documentation
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n  %{gem_name}-%{version}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/



# Run the test suite
%check
pushd .%{gem_instdir}
%if 0%{?fedora} > 21
rspec2 -Ilib spec
%else
rspec -Ilib spec
%endif
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/sensu-json.gemspec

%changelog
* Tue Dec 20 2016 Martin Mágr <mmagr@redhat.com> - 2.0.1-1
- Updated to latest upstream

* Mon May 09 2016 Martin Mágr <mmagr@redhat.com> - 1.1.1-3
- Explicitly list provides for RHEL
- Use virtual require for Oj

* Mon May 02 2016 para <mmagr@redhat.com> - 1.1.1-2
- Add missing runtime dependency

* Mon May 02 2016 para <mmagr@redhat.com> - 1.1.1-1
- Initial package
