#include<linux/kernel.h>
#include<linux/module.h>
#include<linux/netfilter.h>
#include<linux/netfilter_ipv4.h>
#include<linux/init.h>
#include<linux/skbuff.h>
#include<linux/vmalloc.h>
#include<linux/slab.h>
#include<linux/list.h>
#include<linux/tcp.h>
#include<linux/udp.h>
#include<linux/ip.h>
#include<linux/proc_fs.h>


static struct nf_hook_ops nfho;
#define DESCRIPTION "Basic firewall to drop all packets"
MODULE_AUTHOR ("Suresh Nagulavancha");
MODULE_LICENSE ("GPL");
MODULE_DESCRIPTION (DESCRIPTION);


//function to be called by hook

unsigned int hook_func_incoming(unsigned int hooknum,struct sk_buff *skb,
                                const struct net_device *in,
                                const struct net_device *out,
                                int (*okfn)(struct sk_buff *))
{
        //going to write
	return NF_DROP;
}


//called when module loaded first time

static int __init fw_start(void)
{
//function to call for conditions met
nfho.hook=hook_func_incoming;
//called after packet received
nfho.hooknum=NF_INET_PRE_ROUTING;
//IPV4 packets
nfho.pf=PF_INET;
//priority setting
nfho.priority=NF_IP_PRI_FIRST;
//register hook
nf_register_hook(&nfho);
//printing kernel info
printk(KERN_INFO "simple firewall loaded\n");
return 0;
}
//called when module is unloaed
static void __exit fw_end(void)
{
printk(KERN_INFO "simple firewall unloaded\n");
nf_unregister_hook(&nfho);
}
module_init(fw_start);
module_exit(fw_end);



