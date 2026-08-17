#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
╔══════════════════════════════════════════════════════════════════╗
║     🔐 CyberSecurity Toolkit Pro v2.0                          
║     By STYVEN Emmanuel                                         
║     Full Security Suite - Termux Compatible                   
╚══════════════════════════════════════════════════════════════════╝
"""

import subprocess
import socket
import dns.resolver
import whois
import requests
import json
import os
import sys
import time
import hashlib
import base64
import re
import threading
import queue
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlparse
import ssl
import csv
import ipaddress

# ===================== COLORS =====================
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    WHITE = '\033[97m'
    MAGENTA = '\033[35m'

# ===================== BANNER =====================
def banner():
    os.system('clear')
    print(f"""
{Colors.RED}╔══════════════════════════════════════════════════════════════════╗
{Colors.GREEN}║                                                                  
{Colors.CYAN}║     🔐 CYBERSECURITY TOOLKIT PRO v2.0                           
{Colors.YELLOW}║     By STYVEN Emmanuel                                         
{Colors.MAGENTA}║     Full Security Suite - 30+ Tools Integrated               
{Colors.GREEN}║                                                                  
{Colors.RED}╚══════════════════════════════════════════════════════════════════╝
{Colors.END}
{Colors.WHITE}📱 WhatsApp: https://whatsapp.com/channel/0029VbCUG0XHltYAlmcp9A3T

📺 Telegram: https://t.me/StyvenEmmanuelDev

🐙 GitHub: https://github.com/Styven-Emmanuel-Dev 
{Colors.END}
    """)

# ===================== MAIN TOOLKIT CLASS =====================
class CyberSecurityToolkit:
    def __init__(self, target=None):
        self.target = target
        self.results = {}
        self.start_time = datetime.now()
        self.wordlist = self.load_wordlist()
        
    def load_wordlist(self):
        """Charge la wordlist intégrée"""
        wordlist = [
            'admin', 'test', 'dev', 'api', 'cdn', 'static', 'media',
            'blog', 'forum', 'shop', 'store', 'app', 'mobile', 'portal',
            'secure', 'vpn', 'mail', 'webmail', 'cpanel', 'whm', 'ftp',
            'ssh', 'smtp', 'pop3', 'imap', 'dns', 'ns1', 'ns2', 'www',
            'web', 'server', 'cloud', 'backup', 'db', 'mysql', 'pgsql',
            'redis', 'mongo', 'elastic', 'kibana', 'grafana', 'prometheus',
            'jenkins', 'gitlab', 'github', 'bitbucket', 'jira', 'confluence',
            'wordpress', 'joomla', 'drupal', 'magento', 'prestashop',
            'shopify', 'woocommerce', 'laravel', 'symfony', 'django',
            'rails', 'node', 'react', 'angular', 'vue', 'svelte'
        ]
        return wordlist

    # ===================== DNS TOOLS =====================
    def dns_recon(self):
        """Reconnaissance DNS avancée"""
        print(f"{Colors.BLUE}[*] DNS Reconnaissance...{Colors.END}")
        dns_data = {}
        
        record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'SOA', 'CNAME', 'PTR', 'SRV', 'CAA']
        
        for record in record_types:
            try:
                answers = dns.resolver.resolve(self.target, record)
                dns_data[record] = [str(r) for r in answers]
            except:
                dns_data[record] = ['Not Found']
        
        self.results['dns'] = dns_data
        return dns_data

    def reverse_dns(self):
        """Reverse DNS Lookup"""
        print(f"{Colors.BLUE}[*] Reverse DNS...{Colors.END}")
        try:
            ip = socket.gethostbyname(self.target)
            result = socket.gethostbyaddr(ip)
            self.results['reverse_dns'] = result[0]
            return result[0]
        except:
            self.results['reverse_dns'] = 'Not Found'
            return None

    def dnssec_check(self):
        """Vérification DNSSEC"""
        print(f"{Colors.BLUE}[*] DNSSEC Check...{Colors.END}")
        try:
            result = subprocess.run(['dig', '+dnssec', self.target], 
                                  capture_output=True, text=True)
            if 'ad' in result.stdout or 'flags:' in result.stdout:
                self.results['dnssec'] = 'Enabled'
                return '✅ DNSSEC Enabled'
            else:
                self.results['dnssec'] = 'Disabled'
                return '❌ DNSSEC Disabled'
        except:
            self.results['dnssec'] = 'Unknown'
            return '❓ Unknown'

    # ===================== NETWORK TOOLS =====================
    def advanced_port_scan(self):
        """Scan de ports avancé avec détection de services"""
        print(f"{Colors.BLUE}[*] Advanced Port Scanning...{Colors.END}")
        open_ports = []
        services = {}
        
        common_ports = {
            21: 'FTP', 22: 'SSH', 23: 'Telnet', 25: 'SMTP', 53: 'DNS',
            80: 'HTTP', 110: 'POP3', 111: 'RPC', 135: 'MSRPC', 139: 'NetBIOS',
            143: 'IMAP', 443: 'HTTPS', 445: 'SMB', 993: 'IMAPS', 995: 'POP3S',
            1723: 'PPTP', 3306: 'MySQL', 3389: 'RDP', 5432: 'PostgreSQL',
            5900: 'VNC', 6379: 'Redis', 8080: 'HTTP-Alt', 8443: 'HTTPS-Alt',
            27017: 'MongoDB', 9200: 'Elasticsearch', 11211: 'Memcached'
        }
        
        try:
            ip = socket.gethostbyname(self.target)
            
            for port, service in common_ports.items():
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.3)
                result = sock.connect_ex((ip, port))
                if result == 0:
                    open_ports.append(port)
                    services[port] = service
                sock.close()
            
            self.results['open_ports'] = open_ports
            self.results['services'] = services
            return services
        except:
            self.results['open_ports'] = ['Resolution Error']
            return {}

    def traceroute_analysis(self):
        """Analyse Traceroute"""
        print(f"{Colors.BLUE}[*] Traceroute Analysis...{Colors.END}")
        try:
            result = subprocess.run(['traceroute', '-n', self.target], 
                                  capture_output=True, text=True, timeout=30)
            lines = result.stdout.split('\n')
            hops = []
            for line in lines[1:]:
                if line.strip():
                    parts = line.split()
                    if len(parts) >= 2:
                        hops.append(parts[1])
            self.results['traceroute'] = hops
            return hops
        except:
            self.results['traceroute'] = ['Not Available']
            return []

    def ping_analysis(self):
        """Analyse Ping"""
        print(f"{Colors.BLUE}[*] Ping Analysis...{Colors.END}")
        try:
            result = subprocess.run(['ping', '-c', '4', self.target], 
                                  capture_output=True, text=True)
            times = re.findall(r'time=(\d+\.\d+)', result.stdout)
            if times:
                avg_time = sum(float(t) for t in times) / len(times)
                self.results['ping'] = {
                    'avg_ms': round(avg_time, 2),
                    'packets': len(times)
                }
                return f"✅ Average: {round(avg_time, 2)}ms"
            else:
                self.results['ping'] = {'error': 'No response'}
                return '❌ No response'
        except:
            self.results['ping'] = {'error': 'Failed'}
            return '❌ Failed'

    # ===================== SUBDOMAIN TOOLS =====================
    def subdomain_enumeration(self):
        """Énumération complète des sous-domaines"""
        print(f"{Colors.BLUE}[*] Subdomain Enumeration...{Colors.END}")
        found_subdomains = []
        wordlist = self.wordlist
        
        def check_subdomain(sub):
            subdomain = f"{sub}.{self.target}"
            try:
                socket.gethostbyname(subdomain)
                return subdomain
            except:
                return None
        
        with ThreadPoolExecutor(max_workers=20) as executor:
            futures = {executor.submit(check_subdomain, sub): sub for sub in wordlist}
            
            for future in as_completed(futures):
                result = future.result()
                if result:
                    found_subdomains.append(result)
                    print(f"{Colors.GREEN}✅ {result}{Colors.END}")
        
        self.results['subdomains'] = found_subdomains
        return found_subdomains

    def subdomain_bruteforce(self):
        """Bruteforce de sous-domaines avec wordlist étendue"""
        print(f"{Colors.BLUE}[*] Subdomain Bruteforce...{Colors.END}")
        extended_wordlist = self.wordlist + [
            'mail', 'webmail', 'cpanel', 'whm', 'ftp', 'ssh', 'smtp', 'pop3',
            'imap', 'dns1', 'dns2', 'ns1', 'ns2', 'www2', 'www3', 'web',
            'server', 'cloud', 'backup', 'db', 'mysql', 'pgsql', 'redis',
            'mongo', 'elastic', 'kibana', 'grafana'
        ]
        
        found = []
        for sub in extended_wordlist:
            subdomain = f"{sub}.{self.target}"
            try:
                socket.gethostbyname(subdomain)
                found.append(subdomain)
                print(f"{Colors.GREEN}✅ {subdomain}{Colors.END}")
            except:
                pass
        
        self.results['bruteforce_subdomains'] = found
        return found

    # ===================== WEB TOOLS =====================
    def http_headers_analysis(self):
        """Analyse complète des en-têtes HTTP"""
        print(f"{Colors.BLUE}[*] HTTP Headers Analysis...{Colors.END}")
        headers_data = {}
        
        for protocol in ['https://', 'http://']:
            try:
                url = f"{protocol}{self.target}"
                response = requests.get(url, timeout=5, verify=False, 
                                      headers={'User-Agent': 'Mozilla/5.0'})
                headers_data[protocol] = dict(response.headers)
                self.results['http_headers'] = headers_data
                return headers_data
            except:
                continue
        
        self.results['http_headers'] = {'error': 'No HTTP response'}
        return {'error': 'No HTTP response'}

    def security_headers_analysis(self):
        """Analyse des en-têtes de sécurité"""
        print(f"{Colors.BLUE}[*] Security Headers Analysis...{Colors.END}")
        security_headers = {
            'Strict-Transport-Security': 'HSTS',
            'Content-Security-Policy': 'CSP',
            'X-Frame-Options': 'Clickjacking Protection',
            'X-Content-Type-Options': 'MIME Sniffing Protection',
            'X-XSS-Protection': 'XSS Protection',
            'Referrer-Policy': 'Referrer Policy',
            'Permissions-Policy': 'Permissions Policy',
            'Cross-Origin-Embedder-Policy': 'COEP',
            'Cross-Origin-Opener-Policy': 'COOP',
            'Cross-Origin-Resource-Policy': 'CORP'
        }
        
        headers = self.results.get('http_headers', {})
        results = {}
        
        for protocol, header_dict in headers.items():
            results[protocol] = {}
            for header, description in security_headers.items():
                value = header_dict.get(header, '❌ Missing')
                results[protocol][header] = {
                    'value': value,
                    'description': description,
                    'status': '✅' if 'Missing' not in value else '❌'
                }
        
        self.results['security_headers'] = results
        return results

    def ssl_tls_analysis(self):
        """Analyse SSL/TLS complète"""
        print(f"{Colors.BLUE}[*] SSL/TLS Analysis...{Colors.END}")
        try:
            context = ssl.create_default_context()
            with socket.create_connection((self.target, 443), timeout=5) as sock:
                with context.wrap_socket(sock, server_hostname=self.target) as ssock:
                    cert = ssock.getpeercert()
                    
                    ssl_info = {
                        'issuer': dict(x[0] for x in cert['issuer']),
                        'subject': dict(x[0] for x in cert['subject']),
                        'not_after': cert['notAfter'],
                        'not_before': cert['notBefore'],
                        'version': cert['version'],
                        'serial_number': cert['serialNumber'],
                        'cipher': ssock.cipher(),
                        'protocol': ssock.version()
                    }
                    
                    # Vérification de la date d'expiration
                    expiry = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
                    days_left = (expiry - datetime.now()).days
                    ssl_info['days_left'] = days_left
                    
                    if days_left < 30:
                        ssl_info['status'] = '⚠️ Expiring soon'
                    elif days_left < 0:
                        ssl_info['status'] = '❌ Expired'
                    else:
                        ssl_info['status'] = '✅ Valid'
                    
                    self.results['ssl'] = ssl_info
                    return ssl_info
        except:
            self.results['ssl'] = {'error': 'SSL not available'}
            return {'error': 'SSL not available'}

    def cms_detection(self):
        """Détection de CMS"""
        print(f"{Colors.BLUE}[*] CMS Detection...{Colors.END}")
        cms_signatures = {
            'WordPress': ['wp-content', 'wp-includes', 'wp-json'],
            'Joomla': ['joomla', 'com_content', 'index.php?option'],
            'Drupal': ['drupal', 'sites/all', 'modules/system'],
            'Magento': ['magento', 'skin/frontend', 'app/code'],
            'Prestashop': ['prestashop', 'modules/', 'themes/'],
            'Shopify': ['shopify', 'cdn.shopify', 'myshopify.com'],
            'WooCommerce': ['woocommerce', 'product-category', 'wc-api'],
            'Laravel': ['laravel', 'public/css', 'public/js'],
            'Django': ['django', 'static/admin', 'admin/login'],
            'React': ['react', 'main.chunk.js', 'static/js'],
            'Angular': ['angular', 'main.js', 'polyfills.js'],
            'Vue.js': ['vue', 'app.js', 'chunk-vendors']
        }
        
        detected = []
        headers = self.results.get('http_headers', {})
        
        for cms, signatures in cms_signatures.items():
            found = False
            for protocol, header_dict in headers.items():
                for sig in signatures:
                    if sig in str(header_dict).lower():
                        found = True
                        break
                if found:
                    break
            
            if found:
                detected.append(cms)
        
        self.results['cms'] = detected
        return detected

    def technology_stack(self):
        """Détection de la stack technologique"""
        print(f"{Colors.BLUE}[*] Technology Stack Detection...{Colors.END}")
        tech = {}
        
        headers = self.results.get('http_headers', {})
        for protocol, header_dict in headers.items():
            # Server
            tech['server'] = header_dict.get('Server', 'Unknown')
            
            # PHP Version
            if 'X-Powered-By' in header_dict:
                tech['x-powered-by'] = header_dict['X-Powered-By']
            
            # Framework detection
            if 'X-Generator' in header_dict:
                tech['generator'] = header_dict['X-Generator']
            
            # Cache
            tech['cache'] = header_dict.get('Cache-Control', 'Not set')
        
        self.results['technology'] = tech
        return tech

    # ===================== SECURITY TOOLS =====================
    def whois_analysis(self):
        """Analyse WHOIS complète"""
        print(f"{Colors.BLUE}[*] WHOIS Analysis...{Colors.END}")
        try:
            w = whois.whois(self.target)
            
            whois_data = {
                'domain_name': w.domain_name,
                'registrar': w.registrar,
                'creation_date': str(w.creation_date),
                'expiration_date': str(w.expiration_date),
                'updated_date': str(w.updated_date),
                'name_servers': w.name_servers,
                'status': w.status,
                'emails': w.emails,
                'country': w.country,
                'org': w.org,
                'dnssec': w.dnssec
            }
            
            # Vérification de l'expiration
            if w.expiration_date:
                days_left = (w.expiration_date - datetime.now()).days
                whois_data['days_to_expire'] = days_left
                if days_left < 30:
                    whois_data['expiry_status'] = '⚠️ Expiring soon'
                elif days_left < 0:
                    whois_data['expiry_status'] = '❌ Expired'
                else:
                    whois_data['expiry_status'] = '✅ Valid'
            
            self.results['whois'] = whois_data
            return whois_data
        except Exception as e:
            self.results['whois'] = {'error': str(e)}
            return {'error': str(e)}

    def geo_ip_analysis(self):
        """Analyse géo-IP complète"""
        print(f"{Colors.BLUE}[*] Geo-IP Analysis...{Colors.END}")
        try:
            ip = socket.gethostbyname(self.target)
            response = requests.get(f'http://ip-api.com/json/{ip}?fields=all', timeout=5)
            data = response.json()
            
            geo_data = {
                'ip': data.get('query', ip),
                'country': data.get('country', 'N/A'),
                'country_code': data.get('countryCode', 'N/A'),
                'region': data.get('regionName', 'N/A'),
                'city': data.get('city', 'N/A'),
                'zip': data.get('zip', 'N/A'),
                'latitude': data.get('lat', 'N/A'),
                'longitude': data.get('lon', 'N/A'),
                'timezone': data.get('timezone', 'N/A'),
                'isp': data.get('isp', 'N/A'),
                'org': data.get('org', 'N/A'),
                'as': data.get('as', 'N/A'),
                'mobile': data.get('mobile', False),
                'proxy': data.get('proxy', False),
                'hosting': data.get('hosting', False)
            }
            
            self.results['geo'] = geo_data
            return geo_data
        except:
            self.results['geo'] = {'error': 'Geo-IP not available'}
            return {'error': 'Geo-IP not available'}

    def dns_zone_transfer(self):
        """Test de transfert de zone DNS"""
        print(f"{Colors.BLUE}[*] DNS Zone Transfer Test...{Colors.END}")
        try:
            ns_servers = dns.resolver.resolve(self.target, 'NS')
            for ns in ns_servers:
                ns_name = str(ns)
                try:
                    zone_transfer = dns.query.xfr(ns_name, self.target, timeout=5)
                    zone = []
                    for message in zone_transfer:
                        for rrset in message.answer:
                            zone.append(str(rrset))
                    if zone:
                        self.results['zone_transfer'] = {
                            'status': '⚠️ VULNERABLE',
                            'ns': ns_name,
                            'zone': zone[:10]  # Limiter les résultats
                        }
                        return '⚠️ Zone Transfer Vulnerable!'
                except:
                    continue
            
            self.results['zone_transfer'] = {'status': '✅ Secure'}
            return '✅ Zone Transfer Secure'
        except:
            self.results['zone_transfer'] = {'status': 'Unknown'}
            return '❓ Unknown'

    def email_spoofing_check(self):
        """Vérification des enregistrements anti-spoofing"""
        print(f"{Colors.BLUE}[*] Email Security Check...{Colors.END}")
        results = {}
        
        # SPF Check
        try:
            spf = dns.resolver.resolve(self.target, 'TXT')
            spf_records = [str(r) for r in spf if 'spf' in str(r).lower()]
            results['spf'] = spf_records if spf_records else '❌ No SPF'
        except:
            results['spf'] = '❌ No SPF'
        
        # DMARC Check
        try:
            dmarc = f"_dmarc.{self.target}"
            dmarc_rec = dns.resolver.resolve(dmarc, 'TXT')
            results['dmarc'] = [str(r) for r in dmarc_rec]
        except:
            results['dmarc'] = '❌ No DMARC'
        
        # DKIM Check
        try:
            dkim = f"default._domainkey.{self.target}"
            dkim_rec = dns.resolver.resolve(dkim, 'TXT')
            results['dkim'] = '✅ DKIM Found'
        except:
            results['dkim'] = '❌ No DKIM'
        
        self.results['email_security'] = results
        return results

    def vulnerability_scan(self):
        """Scan de vulnérabilités basiques"""
        print(f"{Colors.BLUE}[*] Vulnerability Scan...{Colors.END}")
        vulns = []
        
        # Check for common vulnerabilities
        headers = self.results.get('http_headers', {})
        
        for protocol, header_dict in headers.items():
            # Check for missing security headers
            security_headers = ['Strict-Transport-Security', 'X-Frame-Options', 
                              'X-Content-Type-Options', 'X-XSS-Protection']
            
            for sec_header in security_headers:
                if sec_header not in header_dict:
                    vulns.append(f'Missing {sec_header} header')
            
            # Check server version disclosure
            if 'Server' in header_dict:
                server = header_dict['Server']
                if any(version in server for version in ['Apache/2.4.7', 'nginx/1.4.6', 'IIS/8.5']):
                    vulns.append(f'Outdated server version: {server}')
        
        # Check for open ports
        open_ports = self.results.get('open_ports', [])
        dangerous_ports = [21, 23, 25, 110, 143, 445, 3389]
        
        for port in dangerous_ports:
            if port in open_ports:
                vulns.append(f'Dangerous service on port {port}')
        
        self.results['vulnerabilities'] = vulns
        return vulns

    def security_scan(self):
        """Scan de sécurité complet"""
        print(f"{Colors.BLUE}[*] Complete Security Scan...{Colors.END}")
        score = 100
        warnings = []
        
        # Check SSL
        ssl_info = self.results.get('ssl', {})
        if 'error' in ssl_info:
            score -= 20
            warnings.append('No SSL/TLS certificate')
        elif ssl_info.get('status') == '⚠️ Expiring soon':
            score -= 10
            warnings.append('SSL certificate expiring soon')
        elif ssl_info.get('status') == '❌ Expired':
            score -= 30
            warnings.append('SSL certificate expired')
        
        # Check security headers
        headers = self.results.get('security_headers', {})
        missing_headers = 0
        for protocol, header_dict in headers.items():
            for header, data in header_dict.items():
                if 'Missing' in data['value']:
                    missing_headers += 1
        
        score -= missing_headers * 5
        
        # Check open ports
        open_ports = self.results.get('open_ports', [])
        if 22 in open_ports:
            warnings.append('SSH port open (check security)')
        if 21 in open_ports:
            warnings.append('FTP port open (insecure)')
        
        # Check email security
        email = self.results.get('email_security', {})
        if '❌ No SPF' in str(email.get('spf', '')):
            score -= 10
            warnings.append('Missing SPF record')
        if '❌ No DMARC' in str(email.get('dmarc', '')):
            score -= 10
            warnings.append('Missing DMARC record')
        
        self.results['security_score'] = {
            'score': max(0, score),
            'warnings': warnings,
            'status': '✅ Good' if score >= 70 else '⚠️ Needs Improvement' if score >= 50 else '❌ Poor'
        }
        
        return self.results['security_score']

    # ===================== UTILITY FUNCTIONS =====================
    def hash_analysis(self):
        """Analyse de hash (MD5, SHA1, SHA256)"""
        print(f"{Colors.BLUE}[*] Hash Analysis...{Colors.END}")
        hashes = {}
        data = f"{self.target}:{datetime.now()}"
        
        hashes['md5'] = hashlib.md5(data.encode()).hexdigest()
        hashes['sha1'] = hashlib.sha1(data.encode()).hexdigest()
        hashes['sha256'] = hashlib.sha256(data.encode()).hexdigest()
        hashes['sha512'] = hashlib.sha512(data.encode()).hexdigest()
        
        self.results['hashes'] = hashes
        return hashes

    def base64_analysis(self):
        """Analyse Base64"""
        print(f"{Colors.BLUE}[*] Base64 Analysis...{Colors.END}")
        data = f"{self.target}-{datetime.now()}"
        encoded = base64.b64encode(data.encode()).decode()
        decoded = base64.b64decode(encoded).decode()
        
        self.results['base64'] = {
            'original': data,
            'encoded': encoded,
            'decoded': decoded
        }
        return self.results['base64']

    # ===================== DISPLAY FUNCTIONS =====================
    def display_table(self, data, title, columns):
        """Affiche un tableau coloré"""
        print(f"\n{Colors.CYAN}┌{'─' * 80}┐{Colors.END}")
        print(f"{Colors.CYAN}│ {Colors.BOLD}{title}{' ' * (78 - len(title))}{Colors.CYAN}│{Colors.END}")
        print(f"{Colors.CYAN}├{'─' * 80}┤{Colors.END}")
        
        for key, value in data.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    if isinstance(sub_value, str) and '✅' in sub_value:
                        color = Colors.GREEN
                    elif isinstance(sub_value, str) and '❌' in sub_value:
                        color = Colors.RED
                    elif isinstance(sub_value, str) and '⚠️' in sub_value:
                        color = Colors.YELLOW
                    else:
                        color = Colors.WHITE
                    
                    print(f"{Colors.CYAN}│{Colors.END} {Colors.BOLD}{key}:{Colors.END} {color}{sub_key} -> {sub_value}{' ' * (78 - len(str(sub_key)) - len(str(sub_value)) - 4)}{Colors.CYAN}│{Colors.END}")
            else:
                if '✅' in str(value):
                    color = Colors.GREEN
                elif '❌' in str(value):
                    color = Colors.RED
                elif '⚠️' in str(value):
                    color = Colors.YELLOW
                else:
                    color = Colors.WHITE
                
                print(f"{Colors.CYAN}│{Colors.END} {Colors.BOLD}{key}:{Colors.END} {color}{str(value)}{' ' * (78 - len(str(key)) - len(str(value)) - 4)}{Colors.CYAN}│{Colors.END}")
        
        print(f"{Colors.CYAN}└{'─' * 80}┘{Colors.END}")

    def display_results(self):
        """Affiche tous les résultats formatés"""
        print(f"\n{Colors.GREEN}╔{'═' * 80}╗{Colors.END}")
        print(f"{Colors.GREEN}║{Colors.BOLD}                 📊 COMPLETE SCAN RESULTS                  {Colors.GREEN}║{Colors.END}")
        print(f"{Colors.GREEN}╚{'═' * 80}╝{Colors.END}")
        
        # DNS
        print(f"\n{Colors.BLUE}▶ DNS RECORDS{Colors.END}")
        for record, values in self.results.get('dns', {}).items():
            color = Colors.GREEN if 'Not Found' not in str(values) else Colors.RED
            print(f"  {record}: {color}{', '.join(values[:3])}{Colors.END}")
        
        # WHOIS
        print(f"\n{Colors.BLUE}▶ WHOIS INFORMATION{Colors.END}")
        whois_data = self.results.get('whois', {})
        for key, value in whois_data.items():
            if value and key != 'error':
                color = Colors.YELLOW if '⚠️' in str(value) else Colors.WHITE
                print(f"  {key}: {color}{value}{Colors.END}")
        
        # Security Score
        score = self.results.get('security_score', {})
        print(f"\n{Colors.BLUE}▶ SECURITY SCORE{Colors.END}")
        print(f"  Score: {Colors.BOLD}{score.get('score', 0)}/100{Colors.END}")
        status = score.get('status', 'Unknown')
        if '✅' in status:
            print(f"  Status: {Colors.GREEN}{status}{Colors.END}")
        elif '⚠️' in status:
            print(f"  Status: {Colors.YELLOW}{status}{Colors.END}")
        else:
            print(f"  Status: {Colors.RED}{status}{Colors.END}")
        
        if score.get('warnings'):
            print(f"\n  {Colors.RED}⚠️ Warnings:{Colors.END}")
            for warning in score.get('warnings', []):
                print(f"    • {Colors.YELLOW}{warning}{Colors.END}")
        
        # Vulnerabilities
        vulns = self.results.get('vulnerabilities', [])
        if vulns:
            print(f"\n{Colors.RED}▶ VULNERABILITIES FOUND{Colors.END}")
            for vuln in vulns:
                print(f"  ❌ {vuln}")
        
        # Subdomains
        subdomains = self.results.get('subdomains', [])
        if subdomains:
            print(f"\n{Colors.GREEN}▶ SUBDOMAINS ({len(subdomains)}){Colors.END}")
            for sub in subdomains[:10]:
                print(f"  ✅ {sub}")
            if len(subdomains) > 10:
                print(f"  ... and {len(subdomains) - 10} more")
        
        # Open Ports
        services = self.results.get('services', {})
        if services:
            print(f"\n{Colors.GREEN}▶ OPEN PORTS & SERVICES{Colors.END}")
            for port, service in services.items():
                print(f"  ✅ {port}: {service}")
        
        # SSL
        ssl_info = self.results.get('ssl', {})
        if 'error' not in ssl_info:
            print(f"\n{Colors.GREEN}▶ SSL/TLS STATUS{Colors.END}")
            print(f"  Status: {ssl_info.get('status', 'Unknown')}")
            print(f"  Days left: {ssl_info.get('days_left', 'N/A')}")
        
        # GeoIP
        geo = self.results.get('geo', {})
        if 'error' not in geo:
            print(f"\n{Colors.GREEN}▶ GEO-IP LOCATION{Colors.END}")
            print(f"  Country: {geo.get('country', 'N/A')}")
            print(f"  City: {geo.get('city', 'N/A')}")
            print(f"  ISP: {geo.get('isp', 'N/A')}")
        
        # CMS
        cms = self.results.get('cms', [])
        if cms:
            print(f"\n{Colors.GREEN}▶ CMS DETECTED{Colors.END}")
            for c in cms:
                print(f"  ✅ {c}")
        
        # Email Security
        email = self.results.get('email_security', {})
        if email:
            print(f"\n{Colors.GREEN}▶ EMAIL SECURITY{Colors.END}")
            for key, value in email.items():
                print(f"  {key}: {value}")
        
        print(f"\n{Colors.GREEN}╔{'═' * 80}╗{Colors.END}")
        print(f"{Colors.GREEN}║{Colors.BOLD}              ✅ SCAN COMPLETED SUCCESSFULLY              {Colors.GREEN}║{Colors.END}")
        print(f"{Colors.GREEN}╚{'═' * 80}╝{Colors.END}")
        
    def save_results_json(self):
        """Sauvegarde des résultats en JSON"""
        filename = f"scan_{self.target}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.results, f, indent=2, default=str)
            return filename
        except Exception as e:
            return None

    def save_results_csv(self):
        """Sauvegarde des résultats en CSV"""
        filename = f"scan_{self.target}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['Category', 'Key', 'Value'])
                
                for category, data in self.results.items():
                    if isinstance(data, dict):
                        for key, value in data.items():
                            writer.writerow([category, key, str(value)[:500]])
                    else:
                        writer.writerow([category, 'value', str(data)[:500]])
            
            return filename
        except Exception as e:
            return None

    def full_scan(self):
        """Exécute tous les scans"""
        banner()
        print(f"{Colors.BOLD}🎯 Target: {Colors.CYAN}{self.target}{Colors.END}\n")
        
        print(f"{Colors.GREEN}┌{'─' * 80}┐{Colors.END}")
        print(f"{Colors.GREEN}│{Colors.BOLD}                   🔍 SCANNING IN PROGRESS                   {Colors.GREEN}│{Colors.END}")
        print(f"{Colors.GREEN}└{'─' * 80}┘{Colors.END}\n")
        
        # Exécution de tous les modules
        self.dns_recon()
        self.reverse_dns()
        self.dnssec_check()
        self.whois_analysis()
        self.geo_ip_analysis()
        self.dns_zone_transfer()
        self.email_spoofing_check()
        self.advanced_port_scan()
        self.traceroute_analysis()
        self.ping_analysis()
        self.subdomain_enumeration()
        self.subdomain_bruteforce()
        self.http_headers_analysis()
        self.security_headers_analysis()
        self.ssl_tls_analysis()
        self.cms_detection()
        self.technology_stack()
        self.vulnerability_scan()
        self.security_scan()
        self.hash_analysis()
        self.base64_analysis()
        
        # Affichage des résultats
        self.display_results()
        
        # Sauvegarde
        json_file = self.save_results_json()
        csv_file = self.save_results_csv()
        
        print(f"\n{Colors.GREEN}📁 Results saved:{Colors.END}")
        if json_file:
            print(f"  ✅ JSON: {json_file}")
        if csv_file:
            print(f"  ✅ CSV: {csv_file}")
        
        # Temps d'exécution
        elapsed = datetime.now() - self.start_time
        print(f"\n{Colors.CYAN}⏱️  Time elapsed: {elapsed}{Colors.END}")
        
        print(f"\n{Colors.GREEN}╔{'═' * 80}╗{Colors.END}")
        print(f"{Colors.GREEN}║{Colors.BOLD}                  THANK YOU FOR USING THIS TOOL               {Colors.GREEN}║{Colors.END}")
        print(f"{Colors.GREEN}║{Colors.BOLD}                  BY STYVEN EMMANUEL                        {Colors.GREEN}║{Colors.END}")
        print(f"{Colors.GREEN}╚{'═' * 80}╝{Colors.END}")

# ===================== MAIN MENU =====================
def main_menu():
    while True:
        banner()
        print(f"""
{Colors.CYAN}╔══════════════════════════════════════════════════════════════════╗
║                        MAIN MENU                                        
╠══════════════════════════════════════════════════════════════════╣
║                                                                        
║  {Colors.GREEN}1.{Colors.END} 🎯 Full Domain Scan (All Tools)                      
║  {Colors.GREEN}2.{Colors.END} 🌐 DNS Reconnaissance                                
║  {Colors.GREEN}3.{Colors.END} 🔌 Port Scanner                                     
║  {Colors.GREEN}4.{Colors.END} 🔗 Subdomain Enumeration                           
║  {Colors.GREEN}5.{Colors.END} 🌍 Geo-IP & WHOIS Analysis                         
║  {Colors.GREEN}6.{Colors.END} 🛡️ Security Headers Analysis                      
║  {Colors.GREEN}7.{Colors.END} 🔒 SSL/TLS Analysis                                
║  {Colors.GREEN}8.{Colors.END} 📧 Email Security Check (SPF/DKIM/DMARC)           
║  {Colors.GREEN}9.{Colors.END} 📡 CMS & Technology Detection                      
║  {Colors.GREEN}10.{Colors.END}🏴 Vulnerability Scan                              
║  {Colors.GREEN}11.{Colors.END}📊 Security Score Analysis                         
║  {Colors.GREEN}12.{Colors.END}📁 Export Results (JSON/CSV)                      
║  {Colors.GREEN}13.{Colors.END}❌ Exit                                              
║                                                                        
╚══════════════════════════════════════════════════════════════════╝
{Colors.END}
        """)
        
        try:
            choice = input(f"{Colors.CYAN}➜ Enter your choice (1-13): {Colors.END}")
            
            if choice == '1':
                target = input(f"{Colors.CYAN}➜ Enter domain/target: {Colors.END}")
                toolkit = CyberSecurityToolkit(target)
                toolkit.full_scan()
                
            elif choice == '2':
                target = input(f"{Colors.CYAN}➜ Enter domain: {Colors.END}")
                toolkit = CyberSecurityToolkit(target)
                toolkit.dns_recon()
                print(f"\n{Colors.GREEN}DNS Records:{Colors.END}")
                for record, values in toolkit.results.get('dns', {}).items():
                    print(f"  {record}: {', '.join(values)}")
                input(f"\n{Colors.CYAN}Press Enter to continue...{Colors.END}")
                
            elif choice == '3':
                target = input(f"{Colors.CYAN}➜ Enter domain/IP: {Colors.END}")
                toolkit = CyberSecurityToolkit(target)
                services = toolkit.advanced_port_scan()
                print(f"\n{Colors.GREEN}Open Ports:{Colors.END}")
                for port, service in services.items():
                    print(f"  ✅ {port}: {service}")
                input(f"\n{Colors.CYAN}Press Enter to continue...{Colors.END}")
                
            elif choice == '4':
                target = input(f"{Colors.CYAN}➜ Enter domain: {Colors.END}")
                toolkit = CyberSecurityToolkit(target)
                subdomains = toolkit.subdomain_enumeration()
                print(f"\n{Colors.GREEN}Subdomains Found: {len(subdomains)}{Colors.END}")
                for sub in subdomains:
                    print(f"  ✅ {sub}")
                input(f"\n{Colors.CYAN}Press Enter to continue...{Colors.END}")
                
            elif choice == '5':
                target = input(f"{Colors.CYAN}➜ Enter domain: {Colors.END}")
                toolkit = CyberSecurityToolkit(target)
                whois = toolkit.whois_analysis()
                geo = toolkit.geo_ip_analysis()
                
                print(f"\n{Colors.GREEN}WHOIS:{Colors.END}")
                for key, value in whois.items():
                    if value and key != 'error':
                        print(f"  {key}: {value}")
                
                print(f"\n{Colors.GREEN}Geo-IP:{Colors.END}")
                for key, value in geo.items():
                    if value and key != 'error':
                        print(f"  {key}: {value}")
                input(f"\n{Colors.CYAN}Press Enter to continue...{Colors.END}")
                
            elif choice == '6':
                target = input(f"{Colors.CYAN}➜ Enter domain: {Colors.END}")
                toolkit = CyberSecurityToolkit(target)
                toolkit.http_headers_analysis()
                security = toolkit.security_headers_analysis()
                
                print(f"\n{Colors.GREEN}Security Headers:{Colors.END}")
                for protocol, headers in security.items():
                    print(f"\n  {protocol}")
                    for header, data in headers.items():
                        print(f"    {data['status']} {header}: {data['value'][:30]}")
                input(f"\n{Colors.CYAN}Press Enter to continue...{Colors.END}")
                
            elif choice == '7':
                target = input(f"{Colors.CYAN}➜ Enter domain: {Colors.END}")
                toolkit = CyberSecurityToolkit(target)
                ssl_info = toolkit.ssl_tls_analysis()
                
                print(f"\n{Colors.GREEN}SSL/TLS Analysis:{Colors.END}")
                for key, value in ssl_info.items():
                    print(f"  {key}: {value}")
                input(f"\n{Colors.CYAN}Press Enter to continue...{Colors.END}")
                
            elif choice == '8':
                target = input(f"{Colors.CYAN}➜ Enter domain: {Colors.END}")
                toolkit = CyberSecurityToolkit(target)
                email = toolkit.email_spoofing_check()
                
                print(f"\n{Colors.GREEN}Email Security:{Colors.END}")
                for key, value in email.items():
                    print(f"  {key}: {value}")
                input(f"\n{Colors.CYAN}Press Enter to continue...{Colors.END}")
                
            elif choice == '9':
                target = input(f"{Colors.CYAN}➜ Enter domain: {Colors.END}")
                toolkit = CyberSecurityToolkit(target)
                toolkit.http_headers_analysis()
                cms = toolkit.cms_detection()
                tech = toolkit.technology_stack()
                
                print(f"\n{Colors.GREEN}CMS Detected:{Colors.END}")
                for c in cms:
                    print(f"  ✅ {c}")
                
                print(f"\n{Colors.GREEN}Technology Stack:{Colors.END}")
                for key, value in tech.items():
                    print(f"  {key}: {value}")
                input(f"\n{Colors.CYAN}Press Enter to continue...{Colors.END}")
                
            elif choice == '10':
                target = input(f"{Colors.CYAN}➜ Enter domain: {Colors.END}")
                toolkit = CyberSecurityToolkit(target)
                toolkit.dns_recon()
                toolkit.advanced_port_scan()
                toolkit.http_headers_analysis()
                vulns = toolkit.vulnerability_scan()
                
                print(f"\n{Colors.RED}Vulnerabilities Found:{Colors.END}")
                if vulns:
                    for vuln in vulns:
                        print(f"  ❌ {vuln}")
                else:
                    print(f"  {Colors.GREEN}✅ No vulnerabilities found{Colors.END}")
                input(f"\n{Colors.CYAN}Press Enter to continue...{Colors.END}")
                
            elif choice == '11':
                target = input(f"{Colors.CYAN}➜ Enter domain: {Colors.END}")
                toolkit = CyberSecurityToolkit(target)
                toolkit.dns_recon()
                toolkit.advanced_port_scan()
                toolkit.http_headers_analysis()
                toolkit.security_headers_analysis()
                toolkit.ssl_tls_analysis()
                toolkit.email_spoofing_check()
                score = toolkit.security_scan()
                
                print(f"\n{Colors.BOLD}Security Score: {score['score']}/100{Colors.END}")
                print(f"Status: {score['status']}")
                if score['warnings']:
                    print(f"\n{Colors.YELLOW}Warnings:{Colors.END}")
                    for warning in score['warnings']:
                        print(f"  ⚠️ {warning}")
                input(f"\n{Colors.CYAN}Press Enter to continue...{Colors.END}")
                
            elif choice == '12':
                target = input(f"{Colors.CYAN}➜ Enter domain: {Colors.END}")
                toolkit = CyberSecurityToolkit(target)
                toolkit.full_scan()
                
            elif choice == '13':
                print(f"\n{Colors.GREEN}👋 Thank you for using CyberSecurity Toolkit Pro!{Colors.END}")
                print(f"{Colors.CYAN}📱 Follow me on Telegram & WhatsApp for updates!{Colors.END}")
                sys.exit(0)
                
            else:
                print(f"{Colors.RED}❌ Invalid choice!{Colors.END}")
                time.sleep(1)
                
        except KeyboardInterrupt:
            print(f"\n\n{Colors.YELLOW}⚠️ Scan interrupted by user{Colors.END}")
            sys.exit(0)
        except Exception as e:
            print(f"{Colors.RED}❌ Error: {str(e)}{Colors.END}")
            input(f"\n{Colors.CYAN}Press Enter to continue...{Colors.END}")

# ===================== START =====================
if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}⚠️ Exiting...{Colors.END}")
        sys.exit(0)