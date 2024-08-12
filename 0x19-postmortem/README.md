# Postmortem: ALX Intranet Sandbox Outage

## Issue Summary

**Duration:**  
Outage occurred on August 12, 2024, from 14:00 to 17:30 UTC.

**Impact:**  
The sandbox environment on the ALX intranet was down, affecting around 60% of users who rely on it for coding exercises and project testing. Users experienced disruptions in accessing their sandboxes, leading to delays in project submissions and hindering their ability to complete assignments.

**Root Cause:**  
The outage was caused by an overload of concurrent users accessing the sandbox environment, leading to system instability and eventual downtime. The system was unable to handle the high volume of connections, causing it to crash.

## Timeline

- **14:00 UTC** - Issue detected by multiple users who reported an inability to access their sandboxes.
- **14:05 UTC** - Peer alerts were sent to mentors via group channels.
- **14:10 UTC** - Mentors acknowledged the issue and advised users to SSH into sandboxes using external terminals (e.g., Ubuntu terminal, Git Bash, Vagrant).
- **14:20 UTC** - Initial investigation suggested the issue was related to a high number of simultaneous users.
- **15:00 UTC** - Misleading investigation paths considered the possibility of network connectivity issues, but these were ruled out after further checks.
- **15:30 UTC** - Issue escalated to the platform's technical support team for further investigation.
- **16:00 UTC** - Technical team confirmed the root cause as system overload due to excessive concurrent users.
- **16:30 UTC** - Steps to restore the system were initiated, including load redistribution and sandbox resource allocation adjustments.
- **17:30 UTC** - Issue resolved, and sandbox environment fully restored. Users were notified to resume normal operations.

## Root Cause and Resolution

**Root Cause:**  
The root cause of the outage was the sandbox environment's inability to handle the high volume of concurrent users. The system's architecture was not optimized for such load, leading to resource exhaustion and eventual downtime. This was primarily due to a lack of sufficient load balancing and resource allocation mechanisms.

**Resolution:**  
To resolve the issue, the technical team redistributed the load by adjusting resource allocation within the sandbox environment. They temporarily increased the server capacity and optimized the load balancer settings to better manage the high volume of concurrent users. Additionally, they initiated a gradual restoration process to ensure system stability before allowing full user access.

## Corrective and Preventative Measures

**Improvements:**
1. **Load Balancing:** Implement more robust load balancing mechanisms to better distribute traffic across the sandbox environment.
2. **Resource Allocation:** Increase server capacity and allocate additional resources to handle peak usage times.
3. **Monitoring:** Enhance monitoring systems to detect and alert on potential overloads before they cause system downtime.
4. **User Education:** Provide users with alternative methods (e.g., SSH access via external terminals) as standard practice during outages.

**Tasks:**
- [ ] Patch and optimize the sandbox server infrastructure to handle higher concurrency.
- [ ] Implement automated scaling for sandbox environments based on user demand.
- [ ] Add detailed monitoring and alerting for sandbox resource usage.
- [ ] Conduct stress testing to identify system limitations and address bottlenecks.
- [ ] Develop and distribute a guide for users on accessing sandboxes via alternative methods during outages.

